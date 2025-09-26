import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { spawn } from "child_process";
import fs from "fs";
import path from "path";

const server = new McpServer({
    name: 'sbp-mcp',
    version: '1.0.0',
    title: 'SBP MCP Server - Knowledge Amplification',
    capabilities: {
        resources: {},
        tools: {},
        prompts: {},
    }
});

// Configuration
const VAULT_ROOT = "/Users/ian/NEUROMANCER";
const IDEAS_DIR = "1_ideas";
const AMPLIFICATION_DIR = "2_domain_amplification";

// Helper function to get vault statistics
function getVaultStats() {
    const ideasPath = path.join(VAULT_ROOT, IDEAS_DIR);
    const ampPath = path.join(VAULT_ROOT, AMPLIFICATION_DIR);
    
    let ideasCount = 0;
    let ampCount = 0;
    
    try {
        if (fs.existsSync(ideasPath)) {
            const files = fs.readdirSync(ideasPath, { recursive: true });
            ideasCount = files.filter(file => file.endsWith('.md')).length;
        }
    } catch (e) {
        console.warn('Error counting ideas files:', e.message);
    }
    
    try {
        if (fs.existsSync(ampPath)) {
            const files = fs.readdirSync(ampPath, { recursive: true });
            ampCount = files.filter(file => file.endsWith('.md')).length;
        }
    } catch (e) {
        console.warn('Error counting amplification files:', e.message);
    }
    
    return {
        ideas_files: ideasCount,
        amplification_files: ampCount,
        total_files: ideasCount + ampCount,
        timestamp: new Date().toISOString()
    };
}

// Helper function to load markdown files from directory
function loadMarkdownFiles(directory) {
    const dirPath = path.join(VAULT_ROOT, directory);
    const files = [];
    
    if (!fs.existsSync(dirPath)) {
        return files;
    }
    
    try {
        const entries = fs.readdirSync(dirPath, { recursive: true });
        for (const entry of entries) {
            if (entry.endsWith('.md')) {
                const filePath = path.join(dirPath, entry);
                try {
                    const content = fs.readFileSync(filePath, 'utf8');
                    const relPath = path.relative(VAULT_ROOT, filePath);
                    files.push({ path: relPath, content });
                } catch (e) {
                    console.warn(`Error reading ${filePath}:`, e.message);
                }
            }
        }
    } catch (e) {
        console.warn(`Error reading directory ${dirPath}:`, e.message);
    }
    
    return files;
}

// Helper function to extract text content from markdown
function extractTextContent(markdown) {
    const lines = markdown.split('\n');
    const contentLines = [];
    let inFrontmatter = false;
    
    for (const line of lines) {
        if (line.trim() === '---' && !inFrontmatter) {
            inFrontmatter = true;
            continue;
        } else if (line.trim() === '---' && inFrontmatter) {
            inFrontmatter = false;
            continue;
        } else if (!inFrontmatter) {
            // Remove markdown formatting
            const cleanLine = line.replace(/\*\*/g, '').replace(/\*/g, '').replace(/#/g, '').trim();
            if (cleanLine) {
                contentLines.push(cleanLine);
            }
        }
    }
    
    return contentLines.join(' ');
}

// Helper function to get embeddings using ollama
async function getEmbeddings(texts) {
    const embeddings = [];
    
    for (const text of texts) {
        try {
            const response = await fetch('http://localhost:11434/api/embeddings', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    model: 'embeddinggemma',
                    prompt: text
                })
            });
            
            if (response.ok) {
                const data = await response.json();
                embeddings.push(data.embedding);
            } else {
                console.warn('Ollama embedding failed, using zero vector');
                embeddings.push(new Array(768).fill(0));
            }
        } catch (e) {
            console.warn('Ollama embedding error:', e.message);
            embeddings.push(new Array(768).fill(0));
        }
    }
    
    return embeddings;
}

// Helper function to calculate cosine similarity
function cosineSimilarity(a, b) {
    const dotProduct = a.reduce((sum, val, i) => sum + val * b[i], 0);
    const magnitudeA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0));
    const magnitudeB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0));
    return dotProduct / (magnitudeA * magnitudeB);
}

// Tool: Get vault status and statistics
server.tool('get_vault_status', "Get vault statistics and server status", {}, {
    title: 'Get Vault Status',
    description: 'Get statistics about the NEUROMANCER vault and SBP server status',
    readOnlyHint: true,
    destructiveHint: false,
    idempotentHint: true,
    openWorldHint: false
}, async () => {
    try {
        const status = getVaultStats();
        return {
            content: [
                {
                    type: "text",
                    text: `Vault Status:
- Ideas files: ${status.ideas_files}
- Amplification files: ${status.amplification_files}
- Total files: ${status.total_files}
- Embedding model: embeddinggemma (via ollama)
- Timestamp: ${status.timestamp}`
                }
            ]
        };
    } catch (error) {
        return {
            content: [
                {
                    type: "text",
                    text: `Error getting vault status: ${error.message}`
                }
            ]
        };
    }
});

// Tool: Find similar notes using semantic similarity
server.tool('find_similar_notes', "Find semantically similar notes in the vault", {
    query: z.string().describe('The text to find similar notes for'),
    num_results: z.number().optional().describe('Number of similar notes to return (default: 5)'),
    threshold: z.number().optional().describe('Similarity threshold (0-1, default: 0.7)')
}, {
    title: 'Find Similar Notes',
    description: 'Find notes in the vault that are semantically similar to the given query',
    readOnlyHint: true,
    destructiveHint: false,
    idempotentHint: false,
    openWorldHint: false
}, async ({ query, num_results = 5, threshold = 0.7 }) => {
    try {
        // Load files from ideas directory
        const files = loadMarkdownFiles(IDEAS_DIR);
        if (files.length < 2) {
            return {
                content: [
                    {
                        type: "text",
                        text: `Not enough files in ${IDEAS_DIR} to find similarities (found ${files.length})`
                    }
                ]
            };
        }
        
        // Extract text content
        const texts = files.map(file => extractTextContent(file.content));
        
        // Get embeddings
        const queryEmbedding = await getEmbeddings([query]);
        const fileEmbeddings = await getEmbeddings(texts);
        
        // Calculate similarities
        const similarities = [];
        for (let i = 0; i < files.length; i++) {
            const similarity = cosineSimilarity(queryEmbedding[0], fileEmbeddings[i]);
            if (similarity >= threshold) {
                similarities.push({
                    file: files[i].path,
                    similarity: similarity,
                    preview: texts[i].substring(0, 200) + '...'
                });
            }
        }
        
        // Sort by similarity and take top results
        similarities.sort((a, b) => b.similarity - a.similarity);
        const topResults = similarities.slice(0, num_results);
        
        let response = `Found ${topResults.length} similar notes for "${query}":\n\n`;
        topResults.forEach((result, index) => {
            const fileName = result.file.split('/').pop().replace('.md', '');
            response += `${index + 1}. ${fileName}\n`;
            response += `   Similarity: ${(result.similarity * 100).toFixed(1)}%\n`;
            response += `   Preview: ${result.preview}\n\n`;
        });
        
        return {
            content: [
                {
                    type: "text",
                    text: response
                }
            ]
        };
    } catch (error) {
        return {
            content: [
                {
                    type: "text",
                    text: `Error finding similar notes: ${error.message}`
                }
            ]
        };
    }
});

// Tool: Get note embeddings
server.tool('get_note_embeddings', "Get embeddings for notes in the vault", {
    note_paths: z.array(z.string()).optional().describe('Specific note paths to get embeddings for (optional)'),
    directory: z.string().optional().describe('Directory to get embeddings for (e.g., "1_ideas", "2_domain_amplification")')
}, {
    title: 'Get Note Embeddings',
    description: 'Get embeddings for notes in the vault for similarity analysis',
    readOnlyHint: true,
    destructiveHint: false,
    idempotentHint: false,
    openWorldHint: false
}, async ({ note_paths, directory = "1_ideas" }) => {
    try {
        // Load files from directory
        const files = loadMarkdownFiles(directory);
        if (files.length === 0) {
            return {
                content: [
                    {
                        type: "text",
                        text: `No files found in ${directory}`
                    }
                ]
            };
        }
        
        // Extract text content
        const texts = files.map(file => extractTextContent(file.content));
        
        // Get embeddings
        const embeddings = await getEmbeddings(texts);
        
        let response = `Embeddings analysis for ${directory}:\n\n`;
        response += `Total files: ${files.length}\n`;
        response += `Embedding dimension: ${embeddings[0]?.length || 0}\n\n`;
        
        if (files.length > 0) {
            response += `Sample files with embeddings:\n\n`;
            files.slice(0, 5).forEach((file, index) => {
                const fileName = file.path.split('/').pop().replace('.md', '');
                response += `${index + 1}. ${fileName}\n`;
                response += `   Path: ${file.path}\n`;
                response += `   Embedding dimension: ${embeddings[index]?.length || 0}\n`;
                response += `   Preview: ${texts[index].substring(0, 100)}...\n\n`;
            });
        }
        
        return {
            content: [
                {
                    type: "text",
                    text: response
                }
            ]
        };
    } catch (error) {
        return {
            content: [
                {
                    type: "text",
                    text: `Error getting embeddings: ${error.message}`
                }
            ]
        };
    }
});

// Tool: Find note pairs for hebbian learning
server.tool('find_note_pairs', "Find semantically similar note pairs for hebbian learning", {
    directory: z.string().optional().describe('Directory to find pairs in (default: "1_ideas")'),
    max_pairs: z.number().optional().describe('Maximum number of pairs to find (default: 50)'),
    threshold: z.number().optional().describe('Similarity threshold for pairs (default: 0.75)')
}, {
    title: 'Find Note Pairs',
    description: 'Find semantically similar note pairs for hebbian learning and knowledge amplification',
    readOnlyHint: true,
    destructiveHint: false,
    idempotentHint: false,
    openWorldHint: false
}, async ({ directory = "1_ideas", max_pairs = 50, threshold = 0.75 }) => {
    try {
        // Load files from directory
        const files = loadMarkdownFiles(directory);
        if (files.length < 2) {
            return {
                content: [
                    {
                        type: "text",
                        text: `Not enough files in ${directory} to find pairs (found ${files.length})`
                    }
                ]
            };
        }
        
        // Extract text content
        const texts = files.map(file => extractTextContent(file.content));
        
        // Get embeddings
        const embeddings = await getEmbeddings(texts);
        
        // Find pairs
        const pairs = [];
        for (let i = 0; i < files.length; i++) {
            for (let j = i + 1; j < files.length; j++) {
                const similarity = cosineSimilarity(embeddings[i], embeddings[j]);
                if (similarity >= threshold) {
                    pairs.push({
                        note1: files[i].path,
                        note2: files[j].path,
                        similarity: similarity,
                        text1_preview: texts[i].substring(0, 200) + '...',
                        text2_preview: texts[j].substring(0, 200) + '...'
                    });
                }
            }
        }
        
        // Sort by similarity and limit results
        pairs.sort((a, b) => b.similarity - a.similarity);
        const topPairs = pairs.slice(0, max_pairs);
        
        let response = `Found ${topPairs.length} note pairs in ${directory}:\n\n`;
        topPairs.forEach((pair, index) => {
            const note1Name = pair.note1.split('/').pop().replace('.md', '');
            const note2Name = pair.note2.split('/').pop().replace('.md', '');
            response += `${index + 1}. ${note1Name} ↔ ${note2Name}\n`;
            response += `   Similarity: ${(pair.similarity * 100).toFixed(1)}%\n`;
            response += `   Preview 1: ${pair.text1_preview}\n`;
            response += `   Preview 2: ${pair.text2_preview}\n\n`;
        });
        
        return {
            content: [
                {
                    type: "text",
                    text: response
                }
            ]
        };
    } catch (error) {
        return {
            content: [
                {
                    type: "text",
                    text: `Error finding note pairs: ${error.message}`
                }
            ]
        };
    }
});

// Tool: Analyze knowledge graph connections
server.tool('analyze_knowledge_graph', "Analyze connections and patterns in the knowledge graph", {
    focus_area: z.string().optional().describe('Specific area to analyze (e.g., "ai agents", "knowledge synthesis")'),
    min_connections: z.number().optional().describe('Minimum number of connections to include (default: 3)')
}, {
    title: 'Analyze Knowledge Graph',
    description: 'Analyze connections and patterns in the knowledge graph to understand concept relationships',
    readOnlyHint: true,
    destructiveHint: false,
    idempotentHint: false,
    openWorldHint: false
}, async ({ focus_area, min_connections = 3 }) => {
    try {
        // Load files from ideas directory
        const files = loadMarkdownFiles(IDEAS_DIR);
        if (files.length < 2) {
            return {
                content: [
                    {
                        type: "text",
                        text: `Not enough files in ${IDEAS_DIR} to analyze knowledge graph (found ${files.length})`
                    }
                ]
            };
        }
        
        // Extract text content
        const texts = files.map(file => extractTextContent(file.content));
        
        // Get embeddings
        const embeddings = await getEmbeddings(texts);
        
        // Find pairs with high similarity
        const pairs = [];
        for (let i = 0; i < files.length; i++) {
            for (let j = i + 1; j < files.length; j++) {
                const similarity = cosineSimilarity(embeddings[i], embeddings[j]);
                if (similarity >= 0.7) {
                    pairs.push({
                        note1: files[i].path,
                        note2: files[j].path,
                        similarity: similarity,
                        text1_preview: texts[i].substring(0, 200) + '...',
                        text2_preview: texts[j].substring(0, 200) + '...'
                    });
                }
            }
        }
        
        // Sort by similarity
        pairs.sort((a, b) => b.similarity - a.similarity);
        
        let response = `Knowledge Graph Analysis:\n\n`;
        response += `Total pairs found: ${pairs.length}\n`;
        response += `Similarity threshold: 0.7\n`;
        response += `Average similarity: ${pairs.length > 0 ? (pairs.reduce((sum, pair) => sum + pair.similarity, 0) / pairs.length * 100).toFixed(1) : 0}%\n\n`;
        
        if (pairs.length > 0) {
            response += `High-connectivity pairs (top 10):\n\n`;
            pairs.slice(0, 10).forEach((pair, index) => {
                const note1Name = pair.note1.split('/').pop().replace('.md', '');
                const note2Name = pair.note2.split('/').pop().replace('.md', '');
                response += `${index + 1}. ${note1Name} ↔ ${note2Name}\n`;
                response += `   Similarity: ${(pair.similarity * 100).toFixed(1)}%\n`;
                response += `   Preview 1: ${pair.text1_preview.substring(0, 80)}...\n`;
                response += `   Preview 2: ${pair.text2_preview.substring(0, 80)}...\n\n`;
            });
        }
        
        return {
            content: [
                {
                    type: "text",
                    text: response
                }
            ]
        };
    } catch (error) {
        return {
            content: [
                {
                    type: "text",
                    text: `Error analyzing knowledge graph: ${error.message}`
                }
            ]
        };
    }
});

async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
}

main();

