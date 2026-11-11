# Luo Language

**Luo is an independent, general-purpose programming language and computing platform being designed from first principles.**

The ambition is to create a language capable of expressing, building, securing, testing, and operating essentially every class of modern software and computing system. Luo is not only an AI language, an LLM wrapper, or a prompt syntax. It must be a serious language for all software. Artificial intelligence is a first-class design target, but it is one domain among many.

Luo is intended to support operating systems, kernels, drivers, desktop and mobile applications, websites, backend services, databases, cloud infrastructure, distributed systems, games, graphics engines, robotics, embedded systems, scientific software, cryptography, automation, neural networks, LLM training and inference, and future forms of computation.

## The central ambition

Design the language we would choose if we could start with the accumulated lessons of modern computing instead of inheriting decades of accidental complexity.

Luo should combine performance; safety; expressive static typing, inference, generics and pattern matching; structured concurrency and parallelism; hardware portability through an intermediate representation; first-class tensors, automatic differentiation and accelerator-aware AI; security and correctness; excellent developer tools; extensibility; and a long-term path to self-hosting. These are design goals, not claims that the current prototype already provides them.

## Luo's own writing system

Luo has **30 original handwritten characters**. They are part of the language's identity and are intended for source code, text processing, tooling, and programming.

The creator's original handwritten reference is the visual authority. Glyphs must not be replaced by Latin letters, Unicode lookalikes, emoji, or approximate geometric symbols. Each character must eventually have its own faithful digital glyph and stable machine representation. No pronunciation, semantic meaning, or translation is assigned without the creator's approval.

The first implementation milestone is to digitize the original glyphs faithfully, define their encoding and text behavior, and make them possible to type and render reliably. Until the original reference artwork is present, this repository records the inventory in text and deliberately does not fabricate glyph artwork.

## Architecture direction

1. Native Luo writing system: original glyphs, text encoding, input methods, font, normalization, and source-file rules.
2. Language specification: syntax, semantics, types, modules, effects, errors, and compatibility rules.
3. Compiler front end: source decoding, lexer, parser, name resolution, type checking, and diagnostics.
4. Intermediate representation: typed, target-independent representation for optimization and analysis.
5. Optimization and execution: compiler optimizations, runtime services, and code generation.
6. Hardware backends: native CPU targets first, followed by GPUs, accelerators, embedded targets, and other architectures.
7. Standard library and system interfaces: memory, collections, files, networking, concurrency, cryptography, graphics, databases, and platform APIs.
8. Developer ecosystem: package manager, build system, formatter, linter, test runner, debugger, profiler, documentation, and editor integrations.
9. AI and numerical platform: tensors, autodiff, model execution, training primitives, distributed workloads, and hardware acceleration.

The first compiler can be bootstrapped using an existing implementation language and toolchain. That is a practical bootstrap strategy, not a limitation on Luo's final ambitions. Self-hosting is a long-term milestone.

## The full goal

Luo should become a coherent language and ecosystem capable of building:

- **Systems:** operating systems, kernels, boot components, drivers, compilers, runtimes, filesystems, databases, storage engines, networking stacks, cloud infrastructure, and distributed services.
- **Applications:** desktop, mobile, web, cross-platform applications, APIs, real-time collaboration, browser engines, productivity tools, and communication platforms.
- **Interactive media:** games, rendering engines, simulations, audio tools, graphics, and creative software.
- **Physical computing:** robotics, automation, embedded devices, microcontrollers, edge systems, control systems, sensors, and real-time software.
- **Scientific computing:** numerical simulation, data processing, visualization, GPU workloads, and specialized accelerators.
- **AI:** neural networks, tensor programs, automatic differentiation, LLM training, fine-tuning, inference, multimodal models, agent systems, retrieval, evaluation, and distributed training/serving.

AI must not force ordinary applications to depend on AI infrastructure. A small command-line utility should remain small and predictable.

The language should offer high performance without abandoning safety; a modern and coherent type system; concurrency designed into the foundations; hardware-independent compilation; AI and tensor capabilities without becoming AI-only; capability-oriented security and verifiability; excellent tooling; a native writing system; and a path to long-term self-sufficiency.

“Ultimate language” does not mean one syntax magically makes every workload optimal. It means a coherent platform that covers low- and high-level programming, offers safe defaults and explicit escape hatches, exposes performance costs, scales from tiny devices to distributed systems, integrates AI and numerical workloads, maintains precise semantics, and evolves without breaking every program.

## Project status

This repository is the beginning of the specification and implementation. It is not yet a usable general-purpose programming language.

- [x] Establish the project goal and broad design principles.
- [x] Record the 30-character creator-defined register without inventing glyph artwork or meanings.
- [x] Establish the intended layered compiler and runtime architecture.
- [x] Record an initial binary-encoding proposal as provisional, not final.
- [ ] Add the creator's original glyph reference artwork.
- [ ] Digitize and review all 30 glyphs against that artwork.
- [ ] Define stable character code points, text encoding, and input methods.
- [ ] Specify lexical rules, syntax, type system, memory model, and execution semantics.
- [ ] Implement a reference lexer, parser, and diagnostic pipeline.
- [ ] Define the first intermediate representation and executable format.
- [ ] Build and test a minimal end-to-end compiler.
- [ ] Grow the standard library, runtime, backends, and tooling.
- [ ] Develop the AI and accelerator stack.
- [ ] Progress toward a self-hosting compiler.

See docs/GOAL.md, docs/ARCHITECTURE.md, and spec/CHARACTER-REGISTER.md.

## Design discipline

Luo distinguishes approved decisions, proposals, and implemented behavior. A proposal is not a language rule until reviewed and accepted. A roadmap item is not a feature until working code and tests demonstrate it. The creator retains authority over the original character designs and any decisions about pronunciation or meaning.

Prefer coherent, testable foundations over rushing into incompatible features.

## License

No license has been selected yet. Until one is added, the repository's contents are not automatically granted an open-source license merely because the repository is public.
