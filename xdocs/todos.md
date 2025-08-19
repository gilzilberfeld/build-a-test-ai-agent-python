# Todos & Outline

## v Demo 1 (simple agent)
## v ex1 -> Separate into two parts: 1. analysis, 2. Test case suggestions
### v part 1.1 is the introduction.
### v Maybe let them write the prompt themselves.
## v Demo 2 (test idea generation, maybe before 1.2)
### v demo 2 looks like exercise 1.2.
### x will need to separate the two parts, both exercise and solution

## v ex2 -> Can also separate into two parts: 1. Categorization, 2. Prioritization
### v Requires a demo.
### v The solution of the prioritization shows numbers, not the test names. It could be what we want, but needs to check.
### v both can be deferred to later, but if we do, we'll need a structured demo/exercise before the complete.

## ex3 -> Has the generation part by LLM and validation.
### v The generation is straight forward prompt. The execution is the tricky part.  Got demo
### v The validation part requires AST, may leave it out. Also it may fail incorrectly
### x Also, need a skip option if the generated code is not valid.
### v If deferred need a demo, Also need to separate 
### v Solution for Validation also includes execution.  Need to do something about it

## Demo 3 (result analysis)
### v ex4 -> Has the code execution part, and analysis results
### v Demo 3 covers the analysis, need demo for code execution.
### v Can also separated.

## ex5-> validation and anomalies. Can be deferred to later.

## Demo 4 (whole process)
## ex6 -> The whole process, from test case generation to execution and analysis.
### It doesen't use the modules created before. Might want to use the modules.

Possible outline:
1. Introduction
2. Demo 1: Simple Agent (learn: prompting)
3. Exercise 1 (part 1): Analysis
4. Demo 2: Test Idea Generation (learn: specific prompting)
5. Exercise 1.2: Test Case Suggestions
6. Demo W: Structured Results (learn: structured results)
7. Exercise 2.1: Categorization
8. Demo X: Code generation (learn: code generation)
9. Exercise 3.1: Test Code Generation
10. Demo Y: Code Execution (learn: code execution)
11. Exercise 4.1: Code Execution
12. 
12. Demo 3: Result Analysis (learn: analyze results)
13. Exercise 4.2: Result Analysis
14. Demo 4: Whole Process (learn: putting it all together)
15. Exercise 6 Whole process.

Advanced Topics:
16. Exercise 2.2: Prioritization
17. Demo Z: For Validation
17. Exercise 3.2: code Validation
19. Exercise 5.1: Result validation
20. Exercise 5.2: Anomalies