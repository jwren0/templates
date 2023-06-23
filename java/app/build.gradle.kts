plugins {
    application
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.junit.jupiter:junit-jupiter:5.9.3")
}

application {
    mainClass.set("example.App")
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}
