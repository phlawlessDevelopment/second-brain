
## Tags
#clojure #concurrency  #lisp #tools #web/backend

## Tooling

### Leiningen (packages)

#### commands:
```
# new project
lein new app <project_name>

# install all dependancies
lein deps
```

## Add a dependency to your project and use it

1.  Include an additional item in the :dependencies specification in your project’s project.clj file.
2.  Run “lein deps” at the command line (which will pull in the necessary files from the web).
3.  Make sure the new stuff is visible to the environment in which you’re running your code; for clooj I quit/restart clooj after running lein deps.

How do you find the item to include in project.clj? That depends on what dependency you want to pull in. Things that are part of Clojure itself can be found at [https://github.com/clojure](https://github.com/clojure), and if you look at the readme text for any of the specific libraries you’ll see what you need to add. For example, clicking on math.combinatorics I see that this is the thing to add to the :dependencies specification for leiningen: [org.clojure/math.combinatorics “0.0.3”]

## Libs

|Name|Type|Notes|Command|
|:---:|:---:|:---:|:---:|





