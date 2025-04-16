class ProjectNotFoundException(Exception):
    def __init__(self, message="Project not found"):
        super().__init__(message)
