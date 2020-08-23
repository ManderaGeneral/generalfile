"""Gather all custom errors here."""

class MiddleGroundError(Exception): """Parent of all middle ground errors."""
class CaseSensitivityError(MiddleGroundError): """Raised when an existing file matches a path but not the exact case."""
class InvalidCharacterError(MiddleGroundError): """Raised when using an invalid character."""





