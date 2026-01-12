# Python-tutorial-template: [REPLACE WITH TITLE]

<!-- 
INSTRUCTIONS FOR INSTRUCTORS:
1. Click "Use this template" to create a new repository
2. Replace all [BRACKETED CONTENT] with your specific information
3. Delete this instruction block
4. Customize sections as needed for your course
5. See TEACHING-NOTES.md for setup instructions
-->

repository template for teaching materials in Python, whether intended for use in a workshop or class, as asynchronous learning materials, or both.
[insert brief description here]

## [Python / Github Best Practices]
* recommendations not requirements!*

1. use R Studio
2. follow project organization best practices (see below)
3. create a virtual environment (currently, the most widely used R tool for this is **renv**) that allows you to create a reproducible, transportable, and sustainable programming environment.
4. ...
5. ...
   
## [Project Folder Organization]

+ Follow a one project - one folder approach
+ within your project folder create a logical and simple structure of sub-folders that can be used consistently across similar projects. 
+ provide files with names that enable quick discovery when sorted in alphabetical order

File-naming convention for our teaching materials:

+ abbreviations:

    + c = course

    + g = group, i.e. a working group

    + re = resources (to distinguish from the **R** programming language)

    + w = workshop

    + ws = workshop series

+ lessons:

    + {top-level, i.e. “R” or “Python}_{short-title}_{w=workshop}_{level}

        + i.e. `R_Essentials_w_beg`  

Recommended file structure and file-naming practices:

```
repository_root_dir
  |-archive (for older versions of material)
  |-data      (for smaller practice datasets to be used with lessons; 
              it is recommended that larger datasets be disseminated in an alternative manner
              to prevent making the repository too large)
  
  |-instructor_notes
  |-lessons
    |-lesson-name (i.e. `01_R-Setup` for a sequential workshop or `R-Setup` for a non-sequential workshop of that name)
      |-code
      |-exercises
      |-lesson-resources
      |-slides
    |-02_lesson
      ...
    |-03_lesson
      ...
  |-other
  |-resources
  |-solutions
  ...
  
 ```


# REPLACE THE ABOVE WITH AN OVERVIEW OF YOUR WORKSHOP / COURSE / TUTORIAL SERIES

## 1. Overview

## 2. Creator(s) / Author(s)

## 3. Designed for:

+ in-person, virtual, or hybrid workshop?

+ class visit?

+ full course?

+ asynchronous instruction?
  
## 4. Learning Objectives

Upon completing the lessons offered here, the student will be able to:

+ obj 1

+ obj 2

+ obj 3

+ obj 4

+ obj 5

  *recommendations: identify up to 5 principal learning objectives. These objectives should be feasable, measureable...*
  
## 5. Instructor(s) and Years Taught (if taught live)

+ Jane Doe, Research Facilitiation (Intro to R Workshops, W2026 and F2028)
+ John Q Public, Research Computing (R Essentials, F2031)

## 6. Other Instructional Information

**Level:** [Beginner/Intermediate/Advanced]

**Duration:** [length of workshop/course OR estimated time to completion for asynchronous study]

**Pre-requisites:** [required knowledge / skills to begin]

    + 1. pre-req 1

    + 2. pre-req 2
    
## 7. Getting Started

Go to [setup.qmd](setup.qmd) for detailed set up instructions!

### Software Installation

#### Required Software

- **Python** (version 3.10 or higher): Download from [python.org](https://www.python.org/downloads/)
- **Visual Studio Code**: Download from [code.visualstudio.com](https://code.visualstudio.com/)
- **uv** (package manager): Install instructions at [astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/)

#### Installing uv

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

**macOS/Linux**:

```{bash}
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Clone or Download This Repository

Option A: Using Git (recommended)



## 8. Overview of Materials

1. Notebooks / code
2. Slides
3. Other instructional materials
4. Data
   
## Acknowledgements

[Credit any sources, contributors, or funding sources]


**Template Information**: This repository was created using the [Python Tutorial Template](https://github.com/Dartmouth-Libraries/Python-tutorial-template) (created by Research Facilitation, Dartmouth Libraries).


