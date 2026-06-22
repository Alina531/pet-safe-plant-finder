Pet-Safe Plant Finder

Elevator Pitch

A searchable plant recommendation system that helps pet owners find plants that fit their home environment while minimizing toxicity risks.

The system uses structured veterinary data for filtering and AI-generated explanations to make toxicity information easier to understand.

⸻

Core User Problem

The user doesn’t know:

* Which plant to buy
* Whether it is safe for their pet
* Whether it fits their home conditions

The user only knows:

* I have a cat
* My living room is shady
* I want a large plant
* I prefer low maintenance

The system should turn those requirements into recommendations.

⸻

Main User Flow

Step 1 - Select Pets

Examples:

* Cat
* Dog

Future support:

* Bird
* Rabbit
* Reptile
* Other pets

⸻

Step 2 - Select Location

* Indoor
* Outdoor

⸻

Step 3 - Select Light Conditions

* Low Light
* Partial Light
* Full Sun

⸻

Step 4 - Select Plant Size

* Small
* Medium
* Large

⸻

Step 5 - Select Maintenance Level

* Low
* Medium
* High

⸻

Step 6 - View Matching Plants

Examples:

* Spider Plant
* Cast Iron Plant
* Parlor Palm

⸻

Search Experience

The user can search using a single search box.

Examples:

* Spider Plant
* ירקה
* Chlorophytum comosum
* Airplane Plant
* Ribbon Plant

All searches should resolve to the same plant.

The user should never need to know whether the name is:

* Scientific
* Hebrew
* Common name
* Alias

The system handles that automatically.

⸻

Plant Identity Resolution

Problem

The same plant can appear across different sources under different names.

Example:

Spider Plant

May also appear as:

* ירקה
* Chlorophytum comosum
* Airplane Plant
* Ribbon Plant

Without identity resolution:

* Duplicate records may be created
* Search becomes unreliable
* Users may fail to find plants

⸻

Solution

A plant has one canonical identity.

Example:

Plant:

* Chlorophytum comosum

Aliases:

* Spider Plant
* ירקה
* Airplane Plant
* Ribbon Plant

All aliases point to the same plant record.

⸻

User Experience Benefit

If the system recommends:

Spider Plant

and the user sees:

ירקה

at the nursery,

the system should clearly display:

Spider Plant (ירקה)

Scientific Name:
Chlorophytum comosum

Other Names:
Airplane Plant
Ribbon Plant

This allows users to confidently identify the correct plant.

⸻

Database Design

plants

Stores:

* Plant identity
* Scientific name
* Display name
* Description

⸻

plant_aliases

Stores:

* Hebrew names
* Scientific synonyms
* Common names
* Alternative names

Purpose:

Search and identification.

⸻

animals

Stores:

* Cat
* Dog
* Bird
* Future animals

⸻

plant_toxicity

Stores toxicity per:

Plant + Animal

Not per plant alone.

Reason:

A plant can be:

* Safe for dogs
* Dangerous for cats
* Deadly for birds

⸻

Scale Consideration #1 - Normalized Schema

Tables:

* plants
* plant_aliases
* animals
* plant_toxicity

Benefits:

* Easy expansion
* Reduced duplication
* Better search
* Better maintainability

⸻

Scale Consideration #2 - Pagination

Avoid:

Return all plants.

Use:

GET /plants?page=1&page_size=20

Benefits:

* Faster responses
* Lower memory usage
* Better scalability

⸻

Scale Consideration #3 - Database Indexes

Examples:

* plant_aliases.normalized_name
* plant_toxicity.animal_id
* plants.location
* plants.light_condition

Purpose:

Support fast searches as the dataset grows.

Demonstration:

Index Scan

instead of:

Sequential Scan

⸻

AI Integration

What AI Does NOT Do

AI does not:

* Decide whether a plant is safe
* Determine toxicity levels
* Replace the database

All decisions remain deterministic and database-driven.

⸻

What AI DOES Do

AI translates structured toxicity information into human-friendly explanations.

Flow:

Database
→ Structured Data
→ AI
→ Human-Friendly Explanation

Example Input:

{
“plant”: “Dieffenbachia”,
“animal”: “Cat”,
“toxicity”: “Dangerous”,
“symptoms”: [
“drooling”,
“vomiting”,
“mouth irritation”
]
}

Example Output:

“This plant is not usually deadly, but chewing it may cause mouth irritation, drooling and vomiting.

If your cat tends to bite plants, consider choosing a safer alternative.”

⸻

Why This AI Design

Benefits:

* Cheap
* Predictable
* Reliable
* Easy to test
* Easy to maintain

AI is used as an explanation layer, not a decision engine.

⸻

AI Cache Layer

Problem

100 users request:

Dieffenbachia + Cat

There is no reason to generate the same explanation 100 times.

⸻

Solution

Table:

ai_explanations

Fields:

* id
* plant_id
* animal_id
* generated_text
* created_at

⸻

Flow

User requests explanation

↓

Check cache

↓

Explanation exists?

Yes

Return cached explanation.

No

Call AI

↓

Save response

↓

Return response

Benefits:

* Lower AI costs
* Faster responses
* Better scalability

⸻

Trust and Data Quality

The system is NOT the source of truth.

Instead, it is a curated database built from trusted sources.

Examples:

* ASPCA
* Pet Poison Helpline
* Veterinary sources
* Plant databases

Each toxicity record should include:

* Source name
* Source URL
* Last verified date

Goal:

Provide transparent and trustworthy recommendations.

⸻

Technology Stack

Backend:

* FastAPI
* PostgreSQL

Development Tools:

* Docker
* Postman
* pgAdmin

Code Quality:

* Ruff
* Pytest

CI/CD:

* GitHub Actions

Frontend:

* HTML
* Jinja2 Templates

⸻

What This Project Demonstrates

Technical Skills:

* Database Design
* API Development
* Docker
* Testing
* CI/CD

Engineering Thinking:

* Search Architecture
* Identity Resolution
* Scalability Considerations
* Caching
* Performance Awareness

Product Thinking:

* Decision support systems
* User-focused design
* Trusted knowledge management

AI Usage:

* Practical AI integration
* Cost-aware implementation
* Explainability over decision-making

⸻

Core Idea

User provides requirements

↓

System filters structured knowledge

↓

System generates recommendations

↓

AI explains the result

The project is not about identifying plants.

The project is about helping users make better decisions from structured, trustworthy information.