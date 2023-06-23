plugins {
    id("org.jetbrains.kotlin.jvm") version "1.8.10"
    application
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.jetbrains.kotlin:kotlin-test-junit5")
    testImplementation("org.junit.jupiter:junit-jupiter-engine:5.9.3")
}

application {
    mainClass.set("example.AppKt")
}

tasks.named<Test>("test") {
    useJUnitPlatform()
}
