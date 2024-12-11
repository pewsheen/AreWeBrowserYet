# AreWeBrowserYet
 
Are We Browser Yet is a project that tracks the usability of `Servo` Browser Engine through comparing supported features and performance status.

Currently the only thing that's being tracked is the CSS feature coverage of `Servo`.

## How it works

The [chromestatus](https://chromestatus.com/metrics/css/popularity#variable) collects the most used css properties via Chrome's anonymous usage statistics, while `Servo` currently generates the [supported css properties page](https://doc.servo.org/stylo/css-properties.html) in its `Stylo` component documentation.

This simple page just loads and parse through the data and list out the supported css features of `Servo`.

## Future Work

- [x] Setup a GitHub page
- [x] Rework to be built with Zola
- [x] Automatic rebuilding every week
- [x] Host the page on a better domain
- [ ] Add in supported HTML/JS API tracking
- [x] Improve frontend presentation
- [ ] Add in performance tracking
