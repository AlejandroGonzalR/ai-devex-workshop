from pathlib import Path
from typing import List, Tuple

##################################################################
# Microservice variables
##################################################################

APP_TYPES: List[str] = [
    "api",
    "worker",
]

##################################################################
# Jinja2 templates
##################################################################

TEMPLATES: Path = Path(__file__).parent / "templates"


def map_app_templates(package_name: str) -> List[Tuple[str]]:
    pkg_path = package_name.replace(".", "/")

    return [
        # Kotlin sources
        ("app/Application.kt.j2",
         f"src/main/kotlin/{pkg_path}/Application.kt"),

        ("app/HealthController.kt.j2",
         f"src/main/kotlin/{pkg_path}/HealthController.kt"),

        # Resources
        ("app/application.yml.j2", "src/main/resources/application.yml"),

        # Gradle
        ("app/build.gradle.kts.j2", "build.gradle.kts"),
        ("app/settings.gradle.kts.j2", "settings.gradle.kts"),
        ("app/gradlew.j2", "gradlew"),

        # Project files
        ("app/gitignore.j2", ".gitignore"),
        ("app/Dockerfile.j2", "Dockerfile"),
        ("app/README.md.j2", "README.md"),

        # GitHub Actions CI
        ("ci/build-push.yml.j2", ".github/workflows/ci.yml"),

        # Infrastructure as Code
        ("infra/terraform/main.tf.j2", "terraform/main.tf"),
    ]
