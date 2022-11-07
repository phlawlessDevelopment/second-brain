#python #web/fullstack #web/backend 

# About
Django is a fullstack python framework.

# Snippets

## class based views

```python
class ServiceListView(ListView):
	model = Service 
	paginate_by = 10 # 10 per page
	ordering = ['-pk'] # order by created
```

