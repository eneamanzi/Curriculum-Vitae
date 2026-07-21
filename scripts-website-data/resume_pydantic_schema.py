"""Pydantic schema for the generated resume.json - a real, complete structural
validator (types, required fields, date formats) instead of hand-picked
spot-checks. Raises pydantic.ValidationError with every violation listed, not
just the first one found.

Deliberately strict: extra="forbid" on every model means an unexpected/typo'd
key in the built dict fails validation too, not just a missing one.
"""

import re

from pydantic import BaseModel, ConfigDict, Field, field_validator

ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


def _iso_date_validator(v: str) -> str:
    if not ISO_DATE_RE.match(v):
        raise ValueError(f'not an ISO date (YYYY-MM-DD): "{v}"')
    return v


class Location(Strict):
    address: str
    postalCode: str
    city: str = Field(min_length=1)
    countryCode: str = Field(min_length=1)
    region: str = Field(min_length=1)


class Profile(Strict):
    network: str = Field(min_length=1)
    username: str = Field(min_length=1)
    url: str = Field(min_length=1)


class Basics(Strict):
    name: str = Field(min_length=1)
    label: str = Field(min_length=1)
    image: str
    email: str = Field(min_length=1)
    phone: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    location: Location
    profiles: list[Profile]


class Education(Strict):
    institution: str = Field(min_length=1)
    location: str = Field(min_length=1)
    area: str = Field(min_length=1)
    studyType: str = Field(min_length=1)
    startDate: str
    endDate: str
    score: str = Field(min_length=1)
    courses: list[str]
    highlights: list[str] = Field(min_length=1)

    _valid_dates = field_validator("startDate", "endDate")(_iso_date_validator)


class Work(Strict):
    name: str = Field(min_length=1)
    position: str = Field(min_length=1)
    location: str = Field(min_length=1)
    startDate: str
    endDate: str
    summary: str = Field(min_length=1)
    highlights: list[str] = Field(min_length=1)

    _valid_dates = field_validator("startDate", "endDate")(_iso_date_validator)


class Research(Strict):
    name: str = Field(min_length=1)
    location: str = Field(min_length=1)
    startDate: str
    endDate: str
    summary: str = Field(min_length=1)
    highlights: list[str] = Field(min_length=1)

    _valid_dates = field_validator("startDate", "endDate")(_iso_date_validator)


class Project(Strict):
    name: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    highlights: list[str] = Field(min_length=1)
    keywords: list[str]
    course: str = Field(min_length=1)
    category: str = Field(min_length=1)
    id: str = Field(min_length=1)
    importance: int = Field(gt=0)


class Publication(Strict):
    title: str = Field(min_length=1)
    publisher: str = Field(min_length=1)
    releaseDate: str = Field(min_length=1)
    summary: str = Field(min_length=1)


class Skill(Strict):
    name: str = Field(min_length=1)
    level: str
    icon: str
    keywords: list[str] = Field(min_length=1)


class Language(Strict):
    language: str = Field(min_length=1)
    fluency: str = Field(min_length=1)
    icon: str


class Resume(Strict):
    generated: str = Field(alias="_generated", min_length=1)
    basics: Basics
    education: list[Education] = Field(min_length=1)
    work: list[Work] = Field(min_length=1)
    research: list[Research]
    projects: list[Project]
    publications: list[Publication]
    languages: list[Language] = Field(min_length=1)
    skills: list[Skill] = Field(min_length=1)
    softSkills: list[Skill]
    volunteer: list
    awards: list
    certificates: list
    interests: list
    references: list

    model_config = ConfigDict(extra="forbid", populate_by_name=True)
