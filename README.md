# Software I/O Parameter Vocabulary

A small RDF vocabulary for describing named input parameters and filesystem
inputs and outputs of executable software interfaces.

It complements [CodeMeta 3](https://w3id.org/codemeta/3.0), the
[Software Types profile](https://w3id.org/software-types), and the
[Software I/O Data vocabulary](https://w3id.org/software-iodata).

The vocabularies have separate responsibilities:

- `inputParameter`, `inputFile`, `inputFolder`, `outputFile`, and
  `outputFolder` describe the invocation interface.
- `consumesData` and `producesData` describe the semantic data contract.

## Namespace

```text
https://eosc-data-commons.github.io/software-ioparameter/
```

Suggested prefix:

```turtle
@prefix ioparam: <https://eosc-data-commons.github.io/software-ioparameter/> .
```

The w3id.org redirects must be registered before these identifiers are
published.

## Files

- `software-ioparameter.jsonld` — vocabulary in JSON-LD
- `software-ioparameter.ttl` — vocabulary in Turtle
- `context.jsonld` — compact JSON-LD context
- `examples/` — CodeMeta 3 examples

## Model

`Parameter` specialises `schema:PropertyValueSpecification`. Existing
Schema.org properties such as `valueName`, `valueRequired`, `defaultValue`,
`multipleValues`, `valuePattern`, `minValue` and `maxValue` can therefore
be used without redefining them.

Scalar outputs are deliberately not modelled as parameters: a parameter is a
value supplied to an invocation. Files and folders are modelled as first-class
input or output artefacts.

The vocabulary adds:

- `inputParameter` — a non-filesystem value accepted by an interface
- `inputFile` and `inputFolder` — filesystem inputs
- `outputFile` and `outputFolder` — filesystem outputs
- `valueType` — the XSD datatype or semantic class of a parameter value
- `mediaType` and `fileExtension` — file characteristics
- `path` — a filesystem path or path template
- `filePattern` and `recursive` — folder-content selection
- `required` — whether an input file or folder must be supplied

No domain is declared for the input/output relationships. They can be used with
`WebAPI`, `CommandLineApplication`, workflow steps, or other executable
interfaces without causing unintended RDF type inference.

## CodeMeta context

```json
{
  "@context": [
    "https://w3id.org/codemeta/3.0",
    "https://w3id.org/software-types",
    "https://eosc-data-commons.github.io/software-ioparameter/context.jsonld"
  ]
}
```

## Parameter examples

A required string input:

```json
{
  "@type": "Parameter",
  "name": "Shared With",
  "valueName": "shared_with",
  "valueType": "xsd:string",
  "valueRequired": true
}
```

A file input:

```json
{
  "@type": "File",
  "name": "Audio file",
  "identifier": "input_file",
  "fileExtension": ".mp3",
  "mediaType": "audio/mpeg",
  "required": true
}
```

A folder input:

```json
{
  "@type": "Folder",
  "name": "Image collection",
  "identifier": "images",
  "path": "/data/images",
  "filePattern": "*.png",
  "recursive": true,
  "required": true
}
```

See `examples/cernbox.jsonld`, `examples/command-line.jsonld`, and
`examples/files-and-folders.jsonld` for complete CodeMeta records.

## Alignment with semantic I/O data

Invocation parameters and semantic data descriptions can coexist:

```json
{
  "consumesData": {
    "@type": "AudioObject",
    "encodingFormat": "audio/mpeg"
  },
  "inputParameter": {
    "@type": "Parameter",
    "name": "Language",
    "valueName": "language",
    "valueType": "xsd:string",
    "valueRequired": true
  },
  "inputFile": {
    "@type": "File",
    "name": "Audio file",
    "identifier": "input_file",
    "fileExtension": ".mp3",
    "mediaType": "audio/mpeg",
    "required": true
  }
}
```

These statements answer different questions:

- `consumesData`: what kind of data can the software process?
- `inputParameter` and `inputFile`: how are values and files supplied when
  invoking the software?

The two descriptions are intentionally not coupled. A semantic data type can be
supplied through different parameters or interfaces.

## Local validation

```bash
jq empty software-ioparameter.jsonld context.jsonld examples/*.jsonld

python - <<'PY'
from rdflib import Graph

jsonld = Graph().parse("software-ioparameter.jsonld", format="json-ld")
turtle = Graph().parse("software-ioparameter.ttl", format="turtle")

assert set(jsonld) == set(turtle)
print(f"Validated {len(turtle)} triples")
PY
```

## Scope

The vocabulary describes invocation inputs and filesystem outputs only. It does
not define semantic input/output data types, executable software types, runtime
platforms, commands, endpoints, providers, resource requirements, provenance,
or detection confidence.

## Licence

Apache License 2.0. See `LICENSE`.
