# Pre-commit 

## Introduction

**Git hooks** are *shell scripts found in the hidden .git/hooks directory* of a 
Git repository. These scripts trigger actions in response to the specific
events, so they can help you automate your development lifecycle. Although you 
may never have noticed them, every Git repository includes 12 sample scripts.

**Pre-commit** runs the hooks on every commit to automatically point out issues 
in code such as missing semicoluns, trailing whitespace, and debug statements. 
By pointing these issues out before code review, this allows a code reviewer to
focus on the architecture of a change while not wasting time with trivial style
nitpicks.

