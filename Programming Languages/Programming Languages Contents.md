## general purpose languages
	can be used to create almost any peice of software
	

```dataview
	LIST FROM "Programming Languages"
	WHERE  contains(lang_types, "general")
```


## scripting languages
	for exectuing single file scripts

```dataview
	LIST 
	FROM "Programming Languages"
	WHERE contains(lang_types, "scripting")
```

## game development languages
	I've used  in game development 
```dataview
	LIST FROM "Programming Languages"
	WHERE contains(lang_types, "games")
```

## Functional languages
	FP
```dataview
	LIST 
	FROM "Programming Languages"
	WHERE contains(lang_types, "functional")
```


## WebDev languages
	Has great supourt for web development
```dataview
TABLE web_stack 
FROM "Programming Languages"
WHERE contains(lang_types, "web")
```




