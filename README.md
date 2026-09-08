# Software Input/Output Parameter Vocabulary

A small RDF vocabulary for attaching [Bioschemas `FormalParameter`](https://bioschemas.org/FormalParameter) descriptions to software applications and services.

Canonical namespace:

```text
https://w3id.org/software-ioparameter#
```

## Design

The vocabulary adds two relationship properties:

- `ioparam:inputParameter` — a value consumed by software or a service;
- `ioparam:outputParameter` — a value produced by software or a service.

Every parameter is represented as a Bioschemas `FormalParameter`. Existing Schema.org properties describe it:

| Property | Purpose | Example |
| --- | --- | --- |
| `name` | Human-readable name | `Input file` |
| `identifier` | Machine-facing parameter name | `input_file` |
| `description` | Parameter description | `File to upload` |
| `additionalType` | Structural or semantic value type | `ioparam:File`, `xsd:string` |
| `encodingFormat` | Media type or format identifier | `text/csv` |
| `valueRequired` | Whether the input is mandatory | `true` |
| `defaultValue` | Default parameter value | `false` |

The vocabulary defines only structural types missing from the reused vocabularies:

- `ioparam:File`
- `ioparam:Directory` (also covers the user-interface term “folder”)
- `ioparam:Array`

Primitive values reuse XML Schema datatypes, such as `xsd:string`, `xsd:boolean`, `xsd:integer`, `xsd:decimal`, and `xsd:anyURI`. Domain-specific data types should reuse established vocabularies such as EDAM rather than being copied here.

The two relationship properties deliberately have no `rdfs:domain`. This allows them to be used on both `schema:SoftwareApplication` instances and `schema:WebAPI` services without incorrectly inferring that every subject belongs to one of those classes.

## Example

```json
{
  "@type": "FormalParameter",
  "name": "Input file",
  "identifier": "input_file",
  "description": "File to process.",
  "additionalType": "File",
  "encodingFormat": "text/csv",
  "valueRequired": true
}
```

See [`examples/cernbox.jsonld`](examples/cernbox.jsonld) for a complete CodeMeta and Web API example, and [`examples/parameter-types.jsonld`](examples/parameter-types.jsonld) for file, directory, array, and primitive parameters.

## Files

- `context.jsonld` — reusable JSON-LD context
- `software-ioparameter.jsonld` — vocabulary in JSON-LD
- `software-ioparameter.ttl` — vocabulary in Turtle
- `software-ioparameter.shacl.ttl` — lightweight SHACL constraints
- `examples/` — usage examples

## Validate

Install the development dependencies and run the validator:

```bash
python -m pip install -e '.[dev]'
python scripts/validate.py
```

## Licence

Apache License 2.0. See [`LICENSE`](LICENSE).
