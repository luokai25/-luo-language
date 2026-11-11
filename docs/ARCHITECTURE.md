# Luo System Architecture

This is a proposed architecture, not a claim that these subsystems are implemented.

## Principles
- Separate language semantics from machine-specific code generation.
- Keep the compiler front end deterministic and independently testable.
- Validate explicit intermediate representations at every boundary.
- Make memory, concurrency, effects, and failure behavior part of language design.
- Keep optional AI and accelerator capabilities out of the minimum runtime footprint.
- Treat the standard library, package manager, build system, and diagnostics as core product features.
- Preserve compatibility through versioned specifications and conformance tests.

## Layers

### 1. Native text and glyph layer
Owns the 30 creator-defined characters, original reference artwork and provenance, digital vector masters and font outlines, code-point allocation and encoding, input methods, shaping, rendering, normalization, and source-file conventions. Unicode interoperability must be researched. A private-use mapping may help development but is not automatically a permanent interoperable encoding.

### 2. Language specification
Defines tokens, lexical boundaries, grammar, source-file structure, names, scopes, modules, imports, types, inference, generics, compile-time behavior, evaluation order, runtime semantics, memory/resource model, concurrency/effects, errors, panic behavior, and foreign-function interfaces.

### 3. Compiler front end
1. Decode source text.
2. Validate encoding and character usage.
3. Produce tokens with source spans.
4. Parse tokens into a syntax tree.
5. Resolve names and modules.
6. Type-check and validate effects.
7. Produce typed intermediate representation.
8. Emit structured diagnostics.

Every stage needs isolated unit tests and malformed-input tests.

### 4. Intermediate representations
Potential stages include a typed high-level IR preserving language meaning, a lower-level control/data-flow IR for optimization, and a target-oriented representation for instruction selection and register allocation. Each IR needs invariants, validation, serialization rules, and version compatibility.

### 5. Optimization and code generation
Potential capabilities include constant folding and propagation, dead-code elimination, inlining and specialization, escape and alias analysis, loop/vectorization optimization, register allocation, instruction selection, link-time optimization, debug information, and profiling metadata. Optimization must preserve defined behavior. Correctness and differential testing are mandatory.

### 6. Runtime and standard library
The runtime should be modular. Small embedded programs should not need the entire application runtime. Areas include allocation, collections, strings, files, operating-system interfaces, networking, async execution, structured concurrency, synchronization, atomics, time, randomness, cryptography, serialization, and diagnostics.

### 7. Hardware backends
Start with a practical host CPU backend. Add native CPU architectures, portable sandbox targets such as WebAssembly, GPUs/accelerators, embedded and real-time targets, and future/custom architectures based on demonstrated need. Every backend must pass shared conformance tests and document limitations.

### 8. Numerical and AI platform
Separate numerical foundations from higher-level AI frameworks: numeric types, tensor representations, shape/layout reasoning, automatic differentiation, kernel fusion, memory planning, CPU/accelerator execution, model formats/operators, training, inference, evaluation, serving, and distributed execution. Ordinary Luo programs must remain useful without this layer.

### 9. Developer platform
Provide a Luo CLI, project/package manifests, reproducible builds, formatter, linter, unit/integration/property/fuzz tests, debugger, profiler, language server, editor support, documentation, and API reference generation.

## Bootstrap strategy
The first compiler should use a mature host language selected for implementation speed, reliability, and portability. That host language is a bootstrap dependency, not Luo's identity.

1. Build a small reference lexer/parser and specification tests.
2. Add a typed core language and interpreter or simple code generator.
3. Add a native backend and minimal runtime.
4. Implement a compiler subset in Luo.
5. Move compiler stages toward self-hosting.
6. Progressively maintain compiler, standard library, and tooling in Luo.

## Quality gates
A subsystem is implemented only with a written contract, unit and integration tests, defined error behavior, security considerations, performance measurements where relevant, portability notes, and a maturity label: experimental, preview, stable, or deprecated.
