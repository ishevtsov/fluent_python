from dataclasses import dataclass, field

class ClubMember:
	name: str
	guests: list[str] = field(default_factory=list)