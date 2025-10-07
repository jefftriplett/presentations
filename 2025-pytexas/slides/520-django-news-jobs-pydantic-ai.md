# Case Study: Django News Jobs

![right fit](screenshots/django-news-jobs.png)

![inline](qrcodes/jobs-django-news.png)

https://jobs.django-news.com

---

To promote Django and Python jobs to the Django community

![inline](screenshots/django-news-jobs.png)

---

## Django News Jobs

- Built by humans
- Django app
- Maintained by Claude Code
- Jobs use the Pydantic AI framework

---

## Demo

After we touch on Pydantic AI

---

## Pydantic AI Framework

![right fit](screenshots/ai-pydantic.png)

![inline](qrcodes/ai-pydantic.png)

https://ai.pydantic.dev

---

## What is it?

- Framework for building AI-powered applications
- Type-safe, structured outputs
- Built on Pydantic for data validation
- Works with multiple LLM providers

> The Django ORM of working with LLM providers.

---

## Django News Jobs Use Case

### Structured Data Benefits

- Predictable outputs
- Type safety
- Validation built-in
- Easy to test and maintain

---

## Our BaseModel

```python
from pydantic import BaseModel, Field
from pydantic_ai import Agent

class JobOutput(BaseModel):
    title: str = Field(
        description="The title of the job position.",
    )
    description: str = Field(
        description="A detailed description of the job responsibilities and requirements."
    )
    salary_range: list[str] = Field(
        description="The range of the salary offered for the position.",
    )
    location: str = Field(
        description="The job's location.",
    )
    is_django_job: bool = Field(
        description="Indicates if this job is a Django job.",
    )
    company: str = Field(
        description="The name of the company offering the job.",
    )

```

---

# Our prompt

```python
PROMPT: str = """<title>

{title}

</title>

<description>

{description}

</description>
"""
```

---

```python

def parse_job(pk: int):
	job = JobListing.objects.get(pk=pk)

	SYSTEM_PROMPT: str = "Extract the job information. If you aren't sure of an answer, return an empty value."

	prompt: str = PROMPT.format(title=job.title, description=job.description)

    agent = Agent(
        "openai:gpt-5-mini",
        output_type=JobOutput,
        system_prompt=SYSTEM_PROMPT,
    )
    result = agent.run_sync(prompt)

    print(result.output)

    print(result.usage())

```

---


```python
result.output.title='Backend Python Software Engineer (Hybrid)'                                                                                                          JobOutput(
JobOutput(
    title='Backend Python Software Engineer (Hybrid)',
    description="As a Python Developer, you will be responsible for designing, developing, and maintaining our web applications. This position offers the opportunity to
have a real impact in an influential, technology-focused company powering advanced data center simulation and design. You'll collaborate with the development team to
build web applications using Python and the Django framework, write clean and maintainable code, participate in code reviews, perform unit testing and debugging, and
work closely with product managers and architects to deliver scalable solutions.",
    compensation='',
    salary_range=[],
    benefits=[],
    location='Hybrid',
    is_django_job=True,
    company='NVIDIA'
)

Usage(requests=1, request_tokens=831, response_tokens=1021, total_tokens=1852, details={'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 704,
'rejected_prediction_tokens': 0, 'cached_tokens': 0})

```
