As part of my final year project, My team developed an "Automatic Routine Generator using Genetic Algorithm". The aim of the project was to tackle the complex problem of creating timetables for Unversity that deal with theory classes, laboratory classes and breaks.The project is desined to generate routine for only Computer Department of National College of Engineering.

**Team Members**
- Aashis Shah ( 075/BCT/03 ) 
- Basanta Gurung ( 075/BCT/07 )
- Bimal Rai ( 075/BCT/08 ) @Bimalkhimdung
- Milan Maharjan ( 075/BCT/14 ) 


# Project Overview

![Project Landing page ](/Image%20for%20redme/Major%20Project.png)

We have  used the **genetic algorithm** to optimize the general university course scheduling process. Our system generates the routine based on provided inputs such as teacher details, classroom details and lab details. The system generates each class routine as well as individual teacher routine in PDF form which can be downloaded and printed.

The genetic algorithm we used involved iterative processes of generating population, crossover, and mutation until the optimal solution was generated. The algorithm took inputs as constraints, and depending on whether the constraints were essential or desirable, they were categorized as "hard" and "soft" respectively. Hard Constraints are those which is most satisfy in order to genereate routine where Soft constraints are those contraints whitout this routine can be generated

**Hard Constraints**
- Teacher can't have more than one class in same time period.
- One class room can't hold diffrent classes/ Lan at same time.
- Class room must have sufficent capacity for students.
- Lab classes can't be assigned to a class if the lab is pre-occupied.

**Soft Constraints**

- Some classes may need to be scheluled in a particular time.
- Giving 50-minute break after every two class.
- Every leacturer has minimum and maximum limit of weekly workhour.

### Genetic Algorithm 

![Genetic Algorithm Process](/Image%20for%20redme/Genetic%20Algorithm.png)

Genetic algorithms are a type of evolutionary algorithm that is inspired by the process of natural selection. Genetic algorithm is a computing method that simulates natural selection, which is a process in biological evolution. It is a search heuristic that is inspired by Charles 
Darwin’s theory of natural evolution. This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring offspring of  the next generation. In genetic algorithm, a solution is referred to as a chromosome. The 
explanation of basic genetic algorithm steps are as follows:

**Initial Population**

The genetic algorithm starts by generating an initial population. This initial population consists of all the probable solutions to the given problem. The most popular technique for 
initialization is the use of random binary strings. 

**Evaluation of Chromosome and Fitness**

The fitness function helps in establishing the fitness of all individuals in the population. It assigns a fitness score to every individual, which further determines the probability of being chosen for reproduction. The higher the fitness score, the higher the chances of being chosen for reproduction. If the routine had maximum fitness i.e 480, the routne is selected , else if the fitness was less than 480 then the output is sent for crossover. The fitness score was deducted if the routines fail to meet the given constrains by 10 points.

**Crossover**

Crossover is a genetic operator used to vary the programming of a chromosome or chromosomes from one generation to the next. Two strings are picked from the mating pool 
at random to crossover in order to produce superior offspring.

**Mutation**

mutation may be defined as a small random tweak in the chromosome, to get a new solution. It is used to maintain and introduce diversity in the genetic population and is usually applied with a low probability. If the probability is very high, the GA gets reduced to a random search.


## Output Sample


# Output Sample


Output routine for First Year computer

![This is the output sample for first year](/Image%20for%20redme/First%20Year%20Routine.png)

Teacher Routine Sample

![This is the routine for individual Teacher](/Image%20for%20redme/Teacher%20%20routine%20sample.png)







Overall, it was an exciting and challenging project that allowed us to apply our skills and knowledge to real-world problems. I am proud of the outcome and what our team accomplished together.

# Installation Process

You can clone the project as well as download  from https://github.com/Bimalkhimdung/Major_Project.git.

Programming language Used: Python(Dango Framework), HTML, CSS, JavaScript,SQL, MySQL.

You can also install all requiremts using requiremts.txt file.

Once you have directed to project file location open terminal to that directory and type  : 
 -> pip install -r requiremts.txt

if you have any problem contact me at: (https://twitter.com/bimal_khimdung)
Thank You.