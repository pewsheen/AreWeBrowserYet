+++
insert_anchor_links = "left"
title = "Are We Browser Yet"
+++

# Are We Browser Yet

Are We Browser Yet is a simple site that tracks various aspect of the development of the [Servo browser engine](https://github.com/servo/servo).

## What is Servo?

Taken directly from [Servo.org](https://servo.org/):

> Created by Mozilla Research in 2012, the Servo project is a research and development effort. Stewardship of Servo moved from Mozilla Research to the [Linux Foundation](https://www.linuxfoundation.org/) in 2020, where its mission remains unchanged. In 2023 the project moved to [Linux Foundation Europe](https://linuxfoundation.eu/).
> 
> Servo is written in [Rust](https://www.rust-lang.org/), taking advantage of the memory safety properties and concurrency features of the language.
> 
> Since its creation in 2012, Servo has contributed to W3C and WHATWG web standards, reporting specification issues and submitting new cross-browser automated tests, and core team members have co-edited new standards that have been adopted by other browsers. As a result, the Servo project helps drive the entire web platform forward, while building on a platform of reusable, modular technologies that implement web standards.

You can learn more about Servo [here](https://servo.org/about/).

## Why do we need this site?

As the Servo browser engine develops, it would be great to have an easily accessible way to track the trajectory of the development. While Servo already tracks [the scores of WPT test](https://wpt.servo.org/), it's hard to gauge the actual usability of the browser through results of WPT test suites. Hence this site aims to track the coverage of available CSS features and HTML/JS APIs.

## How does the site works?

This site will automatically rebuild itself every week pulling the latest data from Servo and other sources. See each individual pages to learn more about how it handles relevant data.