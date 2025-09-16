---
type: research
category: vision-models
created: 2025-09-13
tags: [vision-models, photo-metadata, vlm, m4-mac, ollama]
status: active
---

# small-footprint vision models for photo metadata

research on high-benchmark vision models for WINTERMUTE vault photo organization

## top small-footprint models (2025)

### apple fastvlm
**repo**: `apple/ml-fastvlm`
**performance**: smallest variant outperforms llava-onevision-0.5b with 85x faster ttft
**size**: 3.4x smaller vision encoder
**mac compatibility**: native mlx support, ios/macos demo available
**benchmark**: state-of-the-art for size class

### smolvlm
**size**: 2b parameters
**performance**: sota performance for memory footprint
**features**: small, fast, memory-efficient multimodal
**license**: apache 2.0 (fully open source)
**compatibility**: excellent for m4 pro 24gb setup

### paligemma
**size**: 3b parameters
**architecture**: siglip-so400m vision encoder + gemma-2b language model
**strengths**: highly versatile, broad visual-language task coverage
**transferability**: designed for wide applicability

## ollama integration (2025)

### available models
- **llama 3.2 vision**: 11b and 90b parameter multimodal models
- **llava 1.6**: 7b, 13b, 34b parameter sizes
- **llava**: original multimodal model with vision encoder + vicuna

### requirements for m4 pro
- **11b models**: requires 8gb+ vram (perfect fit for 24gb unified memory)
- **ollama 0.4+**: required for vision model support
- **metal acceleration**: native apple silicon optimization

### capabilities
- visual data extraction from photos
- structured data output (markdown, json)
- contextual awareness of visual + textual prompts
- ocr and complex text extraction

## photo metadata extraction tools

### existing github solutions

#### focushyper/ai-photo-metadata-tagger
**focus**: automated keyword tagging for photographers
**features**:
- pre-trained ai model integration
- batch processing capabilities
- metadata embedding directly in image files
- hugging face model support

#### photoprism/photoprism
**focus**: ai-powered photo management
**features**:
- automatic tagging and organization
- ollama model support (july 2025 update)
- decentralized web focus
- search performance optimizations
- coordinate mapping for location metadata

#### kruthik-s/ai-powered-image-tagging
**focus**: generative vision-language model tagging
**approach**: uses modern vlm architectures
**output**: natural language descriptions and tags

### metadata extraction capabilities
- **traditional metadata**: exif, iptc, xmp, icc extraction
- **ai-generated metadata**: scene descriptions, object detection
- **keyword extraction**: keybert for meaningful tags
- **tag filtering**: clip for visual relevance validation

## m4 pro optimization strategies

### memory management
- **11b models**: sweet spot for 24gb unified memory
- **batch processing**: process multiple photos efficiently
- **model caching**: keep models loaded to avoid reload overhead

### performance tuning
```bash
# optimize ollama for vision tasks
export OLLAMA_NUM_PARALLEL=1  # vision models are memory intensive
export OLLAMA_MAX_LOADED_MODELS=1
export OLLAMA_FLASH_ATTENTION=1  # if supported
```

### storage considerations
- **model storage**: 6-12gb per vision model
- **cache optimization**: ssd storage recommended
- **batch sizes**: optimize for memory vs speed tradeoff

## natural language metadata examples

### scene description
"a sunset over a mountain lake with pine trees in the foreground, golden hour lighting, serene landscape photography"

### object detection
"people: 2, boats: 1, mountains: background, water: lake, lighting: golden hour"

### contextual tags
"outdoor, landscape, nature, sunset, mountains, lake, pine trees, golden hour, serene, peaceful"

### technical metadata
"lighting: warm/golden, composition: rule of thirds, depth of field: deep focus, camera angle: low angle"