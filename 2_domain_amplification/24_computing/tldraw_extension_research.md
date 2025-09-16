---
type: research
category: computing
created: 2025-09-16
modified: 2025-09-16
tags: [tldraw, api, extension, ai-integration, whiteboard, sdk]
status: complete
priority: high
relates_to: [gutterball-whiteboard, connectome]
---

# tldraw Extension & AI Integration Research

comprehensive analysis of tldraw's plugin/extension system for adding custom functionality, AI integration, and connectome data connectivity to the gutterball whiteboard implementation.

## 1. tldraw's Plugin/Extension System

### Custom Shapes & Tools Architecture

tldraw provides a robust extension system through **ShapeUtil** classes and **BaseBoxShapeTool** implementations:

```typescript
// Custom Shape Definition
export class CardShapeUtil extends ShapeUtil<ICardShape> {
  static override type = 'card'
  static override props = cardShapeProps

  getDefaultProps() {
    return {
      w: 300,
      h: 300,
      color: 'black'
    }
  }

  // Shape rendering
  component(shape: ICardShape) {
    // Custom React component for shape display
  }

  // Selection indicators
  indicator() {
    // Custom selection visual feedback
  }

  // Geometric definition for hit testing
  getGeometry() {
    // Define shape's geometric representation
  }

  // Resize behavior
  onResize() {
    // Handle shape resizing logic
  }
}

// Custom Tool Definition
export class CardShapeTool extends BaseBoxShapeTool {
  static override id = 'card'
  static override initial = 'idle'
  override shapeType = 'card'
}
```

### Shape System Structure

- **Base Properties**: type, position, rotation, opacity (common to all shapes)
- **Props**: shape-specific attributes (width, height, color, custom data)
- **Meta Property**: application-specific metadata for external system integration
- **Three Shape Types**: core shapes (built-in), default shapes (tldraw standard), custom shapes (user-defined)

### UI Overrides System

Custom tools and shapes integrate via the `overrides` prop:

```typescript
const customOverrides: TLUiOverrides = {
  tools(editor, tools, { addDialog }) {
    // Add custom tools to toolbar
    return {
      ...tools,
      card: {
        id: 'card',
        icon: 'card-icon',
        label: 'Card Tool',
        shortcut: 'c',
        onSelect: () => editor.setCurrentTool('card')
      }
    }
  }
}
```

## 2. tldraw's API for Programmatic Interaction

### Editor API - Core Methods

The Editor class provides comprehensive programmatic control:

```typescript
// Shape Creation & Manipulation
editor.createShapes([
  {
    id: createShapeId(),
    type: 'text',
    x: 100,
    y: 100,
    props: {
      text: 'AI Generated Content',
      size: 'large'
    }
  }
])

// Shape Updates
editor.updateShape({
  id: shapeId,
  type: 'geo',
  props: {
    geo: 'rectangle',
    w: 200,
    h: 150
  }
})

// Selection & Focus
editor.select([shapeId])
editor.zoomToFit()

// Style Management
editor.setStyleForNextShapes(DefaultColorStyle, 'blue')
```

### AI-Generated Content Integration

The API enables sophisticated AI integration patterns:

```typescript
// AI Drawing Automation Example
async function generateDiagram(prompt: string) {
  const aiResponse = await callAIService(prompt)

  const shapes = aiResponse.shapes.map(shape => ({
    id: createShapeId(),
    type: shape.type,
    x: shape.x,
    y: shape.y,
    props: shape.properties
  }))

  editor.createShapes(shapes)
  editor.zoomToFit()
}

// Real-time AI Assistance
editor.sideEffects.registerBeforeCreateHandler('shape', (shape) => {
  // Intercept shape creation for AI enhancement
  if (shouldEnhanceWithAI(shape)) {
    return enhanceShapeWithAI(shape)
  }
  return shape
})
```

### Data Visualization Capabilities

The system supports complex data visualization through custom shapes:

```typescript
// Data-Driven Shape Creation
function createDataVisualization(dataset: any[]) {
  const shapes = dataset.map((dataPoint, index) => ({
    id: createShapeId(),
    type: 'data-point',
    x: dataPoint.x * 50,
    y: dataPoint.y * 50,
    props: {
      value: dataPoint.value,
      category: dataPoint.category,
      metadata: dataPoint
    }
  }))

  editor.createShapes(shapes)
}
```

## 3. Real-Time Collaboration Hooks & AI Participants

### Collaboration Architecture

tldraw's collaboration system uses **tldraw sync** with comprehensive hooks:

```typescript
// Real-time Store Integration
const store = useSync({
  uri: 'wss://your-sync-server.com/room-id',
  assets: assetStore
})

// Presence & Awareness
const collaboratorCursors = usePresence(store)
const userPresence = createPresenceStateDerivation(store)
```

### AI NPC Implementation

AI participants can be integrated through the Yjs awareness protocol:

```typescript
// AI NPC Cursor Control
class AINPCController {
  constructor(private yjsDoc: Y.Doc) {
    this.awareness = new awarenessProtocol.Awareness(yjsDoc)
  }

  async moveToArea(x: number, y: number) {
    this.awareness.setLocalStateField('cursor', {
      x, y,
      type: 'ai-assistant',
      name: 'AI Helper'
    })
  }

  async drawSuggestion(shapes: TLShape[]) {
    // Programmatically create shapes as AI participant
    const shapeRecords = shapes.map(s => [s.id, s])
    this.yjsDoc.getMap('shapes').set('shapes', new Map(shapeRecords))
  }
}
```

### Real-time AI Response System

```typescript
// Event-Driven AI Integration
editor.sideEffects.registerAfterCreateHandler('shape', async (record) => {
  if (record.type === 'draw') {
    // Analyze drawing and provide AI suggestions
    const suggestions = await analyzeDrawing(record)

    // Create AI suggestion shapes
    const aiShapes = suggestions.map(s => createSuggestionShape(s))
    editor.createShapes(aiShapes)
  }
})

// Collaborative AI Commands
function handleAICommand(command: string, userId: string) {
  switch (command) {
    case 'organize':
      // AI automatically organizes shapes
      organizeShapesWithAI()
      break
    case 'enhance':
      // AI enhances selected shapes
      enhanceSelectedShapes()
      break
  }
}
```

## 4. Custom UI Components & Panels

### Complete UI Replacement

tldraw supports full UI customization through the `hideUi` prop:

```typescript
function CustomWhiteboardUI() {
  return (
    <div className="tldraw__editor">
      <Tldraw hideUi>
        <CustomAIPanel />
        <CustomToolbar />
        <ConnectomePanel />
      </Tldraw>
    </div>
  )
}

const CustomAIPanel = track(() => {
  const editor = useEditor()

  return (
    <div className="ai-panel">
      <button onClick={() => generateWithAI('diagram')}>
        Generate Diagram
      </button>
      <button onClick={() => analyzeCanvas()}>
        Analyze Canvas
      </button>
      <AIConversationView />
    </div>
  )
})
```

### Component Override System

Specific UI components can be replaced via the `components` prop:

```typescript
const customComponents: TLComponents = {
  Toolbar: CustomAIToolbar,
  StylePanel: ConnectomeStylePanel,
  ContextMenu: EnhancedContextMenu,
  CollaboratorCursor: AICursor
}

<Tldraw components={customComponents} />
```

### AI Integration Panels

```typescript
const AIInteractionPanel = track(() => {
  const editor = useEditor()
  const [aiState, setAIState] = useState<'idle' | 'thinking' | 'drawing'>('idle')

  return (
    <div className="ai-interaction-panel">
      <div className="ai-chat">
        <AIConversation onCommand={(cmd) => executeAICommand(cmd, editor)} />
      </div>

      <div className="ai-tools">
        <button onClick={() => startAIDrawing()}>
          AI Draw Mode
        </button>
        <button onClick={() => optimizeLayout()}>
          Auto-Layout
        </button>
      </div>

      <div className="connectome-integration">
        <ConnectomeDataView />
        <button onClick={() => importFromConnectome()}>
          Import Data
        </button>
      </div>
    </div>
  )
})
```

## 5. Data Export/Import for Connectome Integration

### Snapshot API for External Systems

tldraw provides comprehensive data export/import through snapshots:

```typescript
// Export Canvas Data
function exportToConnectome() {
  const { document, session } = getSnapshot(editor.store)

  // Transform to connectome format
  const connectomeData = {
    nodes: document.shapes.map(shape => ({
      id: shape.id,
      type: shape.type,
      position: { x: shape.x, y: shape.y },
      properties: shape.props,
      metadata: shape.meta
    })),
    connections: findConnections(document.shapes),
    layout: session.camera,
    timestamp: Date.now()
  }

  return await sendToConnectome(connectomeData)
}

// Import from External Systems
async function importFromConnectome(connectomeData: any) {
  const shapes = connectomeData.nodes.map(node => ({
    id: createShapeId(node.id),
    type: node.type,
    x: node.position.x,
    y: node.position.y,
    props: node.properties,
    meta: {
      connectomeId: node.id,
      ...node.metadata
    }
  }))

  const snapshot = {
    document: {
      shapes: new Map(shapes.map(s => [s.id, s])),
      // ... other document state
    },
    session: {
      camera: connectomeData.layout || { x: 0, y: 0, z: 1 }
    }
  }

  loadSnapshot(editor.store, snapshot)
}
```

### Real-time Connectome Sync

```typescript
// Bi-directional Sync System
class ConnectomeSyncManager {
  constructor(private editor: Editor) {
    this.setupChangeListeners()
  }

  private setupChangeListeners() {
    // Listen for canvas changes
    this.editor.store.listen((changes) => {
      const connectomeUpdates = changes
        .filter(change => change.source === 'user')
        .map(change => this.transformToConnectome(change))

      if (connectomeUpdates.length > 0) {
        this.sendToConnectome(connectomeUpdates)
      }
    })

    // Listen for connectome updates
    this.connectomeStream.onUpdate((updates) => {
      const canvasChanges = updates.map(u => this.transformToCanvas(u))
      this.applyChangesToCanvas(canvasChanges)
    })
  }

  private transformToConnectome(change: RecordsDiff<any>) {
    return {
      type: change.added ? 'create' : change.updated ? 'update' : 'delete',
      entityId: change.record.id,
      properties: change.record.props,
      metadata: change.record.meta,
      timestamp: Date.now()
    }
  }
}
```

### Advanced Data Integration Patterns

```typescript
// Live Data Visualization
class LiveDataIntegration {
  async createLiveChart(dataSource: string) {
    // Subscribe to live data
    const dataStream = await connectome.subscribe(dataSource)

    dataStream.onUpdate((newData) => {
      // Update chart shapes with new data
      const chartShapes = this.findChartShapes(dataSource)
      chartShapes.forEach(shape => {
        editor.updateShape({
          id: shape.id,
          type: shape.type,
          props: {
            ...shape.props,
            data: newData,
            lastUpdated: Date.now()
          }
        })
      })
    })
  }

  async exportCanvasAsDataset() {
    const shapes = editor.getCurrentPageShapes()

    return {
      nodes: shapes.map(s => ({
        id: s.id,
        type: s.type,
        attributes: s.props,
        position: { x: s.x, y: s.y },
        relationships: this.findRelatedShapes(s.id)
      })),
      schema: this.inferDataSchema(shapes),
      metadata: {
        exportedAt: Date.now(),
        canvasSize: editor.getViewportScreenBounds(),
        totalShapes: shapes.length
      }
    }
  }
}
```

## Integration Recommendations

### Immediate Implementation Options

1. **Custom AI Shape Tool**: Create an "AI Assistant" shape that can spawn suggestions and interact with users
2. **Connectome Data Panel**: Add a sidebar panel that shows live data from external systems
3. **AI Drawing Commands**: Implement voice or text commands that programmatically create shapes
4. **Smart Connections**: Auto-detect relationships between shapes and visualize them

### Advanced AI Integration Patterns

1. **Context-Aware AI**: Use canvas context to provide relevant suggestions
2. **Collaborative AI NPCs**: AI participants that can join sessions and contribute
3. **Predictive Drawing**: AI that predicts and suggests next drawing actions
4. **Semantic Shape Recognition**: AI that understands drawing intent and enhances shapes

### Connectome Integration Strategy

1. **Real-time Sync**: Bi-directional sync between canvas and external data systems
2. **Live Data Shapes**: Custom shapes that automatically update with external data
3. **Export Pipeline**: Automated export of canvas data to knowledge management systems
4. **Import Workflows**: Import structured data and visualize it as interactive diagrams

The tldraw SDK provides all necessary APIs and extension points to implement sophisticated AI integration and connectome connectivity while maintaining the real-time collaborative features already implemented in the gutterball whiteboard.