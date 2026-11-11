# Luo Implementation Roadmap

This roadmap separates foundations, design decisions, and working implementation. A checked box means the repository contains the corresponding artifact, not that the entire language feature exists.

## Phase 1: Establish the project foundation
- [x] Record the full general-purpose goal.
- [x] Record the original 30-character inventory from creator-supplied descriptions.
- [x] Document the proposed layered architecture.
- [x] Record the 5-bit character-ID idea as an unapproved proposal.
- [x] Add a register-integrity validator and unit test.
- [x] Add continuous integration for the validator and tests.

## Phase 2: Digitize the native writing system
- [ ] Add the original handwritten reference image to the repository without alteration.
- [ ] Create an asset record for each character, LUO-001 through LUO-030.
- [ ] Digitize each glyph as an editable vector master.
- [ ] Compare every vector with the original image and obtain creator approval.
- [ ] Build a font and rendering test page.
- [ ] Test input, copy/paste, serialization, and round-trip behavior.

**Blocking dependency:** the original handwritten reference image must be available in this working project. Text descriptions are not enough to reconstruct the exact strokes, and approximation is prohibited.

## Phase 3: Freeze the text and encoding model
- [ ] Decide how Luo source text maps to interoperable text encodings.
- [ ] Define character identity separately from token identity.
- [ ] Define grapheme boundaries, normalization, invalid input, and versioning.
- [ ] Define source-file framing and metadata.
- [ ] Approve the encoding proposal and publish conformance vectors.

## Phase 4: Specify the core language
- [ ] Define lexical structure and whitespace/comment rules.
- [ ] Define grammar and syntax using the approved native glyphs.
- [ ] Define names, modules, imports, and visibility.
- [ ] Compare candidate type systems and select one deliberately.
- [ ] Specify memory/resource ownership and unsafe boundaries.
- [ ] Specify concurrency, effects, errors, and evaluation order.
- [ ] Write examples and executable conformance cases.

## Phase 5: Build the first compiler
- [ ] Select the bootstrap implementation language.
- [ ] Implement source decoding and lexer.
- [ ] Implement parser and syntax tree.
- [ ] Implement name resolution and type checking.
- [ ] Define and validate typed IR.
- [ ] Build an interpreter or first code-generation path.
- [ ] Add diagnostics, tests, fuzzing, and reproducible builds.

## Phase 6: Grow the platform
- [ ] Native CPU backend and runtime.
- [ ] Standard library and package manager.
- [ ] Debugger, formatter, linter, profiler, and language server.
- [ ] Cross-platform and embedded targets.
- [ ] Concurrency and distributed execution.
- [ ] Graphics, database, networking, and systems libraries.
- [ ] Tensor, autodiff, GPU, and AI runtime capabilities.
- [ ] Self-hosting compiler and standard library.

## Working rule

Do not invent missing glyph details, freeze provisional encodings, or describe roadmap items as implemented. Each major design choice should have a rationale, alternatives considered, tests, and a documented compatibility impact.
