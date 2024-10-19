# treetastic

Helps to decide where to plant trees in cities and parks based on one
or more images.

## purpose

- Noise reduction
- Air quality
- Aesthetics
- Mental health
- Community space

## workflow

1. Image (geotagged) and budget provided
    - Images should look down the middle of street
2. Images passed through API to Python function
3. Images analysed and determines list of ideal pixels for new trees
    - Assigned with score for improvement to area
4. Program iteratively decides which trees are best for an area
5. List of trees and images are returned to the interface

## scoring system

| Selection Criteria                | Weighting |
| ------                            | ------    |
| Existing trees / greenery         | high      |
| Types of building                 | medium    |
| Street / pavement width           | high      |
| Parking spaces                    | medium    |
| Nearby roads based on location    | medium    |

## tech stack

- Python (interacting with AI)
    - OpenCV for image analysis
- JavaScript (API)
- React user interface

## ai

AI will be used to determine which type of trees are best for a situation and
where to plant them, based on parameters in the image such as

- appearance of area
- space available (space could be made available by removing parking spaces)
- nearby roads (based on OpenStreetMap API and image geo-tag)
- types of buildings

It will also determine which areas will benefit most from trees based on a
total budget provided for all the areas in the images.