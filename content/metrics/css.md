+++
insert_anchor_links = "left"
title = "Stylo CSS Coverage"
+++

This page will be automatically built every week showing the status of supported CSS features in [Stylo](https://github.com/servo/stylo), the styling system of Servo.

The data is generated using json file provided by [chromestatus](https://chromestatus.com/metrics/css/popularity#variable) which collects the most used css properties via Chrome's anonymous usage statistics, which will then be compared with [`Stylo`'s supported css properties](https://doc.servo.org/stylo/css-properties.html).

Additional links to relevant specs are provided by [W3C](https://www.w3.org/Style/CSS/).

Servo supports 271 / 271 of the properties that have a usage of over 5%. (while the total css property count is 687)

Property | Usage | Supported by Servo | Relevant Spec
--- | --- | --- | ---
width | 92.33% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#propdef-width), [ED](https://drafts.csswg.org/css-sizing-3/#propdef-width), [ED](https://drafts.csswg.org/css2/#propdef-width), [ED](https://drafts.csswg.org/css2/#propdef-width), [WD](https://www.w3.org/TR/2021/WD-css-sizing-3-20211217/#propdef-width)
height | 91.75% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#propdef-height), [ED](https://drafts.csswg.org/css-sizing-3/#propdef-height), [ED](https://drafts.csswg.org/css2/#propdef-height), [ED](https://drafts.csswg.org/css2/#propdef-height), [WD](https://www.w3.org/TR/2021/WD-css-sizing-3-20211217/#propdef-height)
display | 91.73% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-display), [ED](https://drafts.csswg.org/css-display/#propdef-display), [ED](https://drafts.csswg.org/css2/#propdef-display), [ED](https://drafts.csswg.org/css2/#propdef-display), [CR](https://www.w3.org/TR/2023/CR-css-display-3-20230330/#propdef-display)
padding | 91.22% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-padding), [ED](https://drafts.csswg.org/css-box-3/#propdef-padding), [ED](https://drafts.csswg.org/css-box-4/#propdef-padding), [ED](https://drafts.csswg.org/css2/#propdef-padding), [ED](https://drafts.csswg.org/css2/#propdef-padding), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-padding), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-padding)
margin | 91.20% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-margin), [ED](https://drafts.csswg.org/css-box-3/#propdef-margin), [ED](https://drafts.csswg.org/css-box-4/#propdef-margin), [ED](https://drafts.csswg.org/css2/#propdef-margin), [ED](https://drafts.csswg.org/css2/#propdef-margin), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-margin), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-margin)
position | 91.10% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-position), [ED](https://drafts.csswg.org/css-position-3/#propdef-position), [ED](https://drafts.csswg.org/css2/#propdef-position), [ED](https://drafts.csswg.org/css2/#propdef-position), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-position)
border | 90.73% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border), [ED](https://drafts.csswg.org/css2/#propdef-border), [ED](https://drafts.csswg.org/css2/#propdef-border), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border)
top | 89.85% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-top), [ED](https://drafts.csswg.org/css-position-3/#propdef-top), [ED](https://drafts.csswg.org/css2/#propdef-top), [ED](https://drafts.csswg.org/css2/#propdef-top), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-top)
color | 89.49% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/colors.html#propdef-color), [ED](https://drafts.csswg.org/css-color-3/#color1), [ED](https://drafts.csswg.org/css-color-4/#propdef-color), [ED](https://drafts.csswg.org/css2/#propdef-color), [ED](https://drafts.csswg.org/css2/#propdef-color), [REC](https://www.w3.org/TR/2022/REC-css-color-3-20220118/#color1), [CRD](https://www.w3.org/TR/2024/CRD-css-color-4-20240213/#propdef-color)
left | 89.45% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-left), [ED](https://drafts.csswg.org/css-position-3/#propdef-left), [ED](https://drafts.csswg.org/css2/#propdef-left), [ED](https://drafts.csswg.org/css2/#propdef-left), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-left)
font-size | 89.22% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#propdef-font-size), [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-size), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-size), [ED](https://drafts.csswg.org/css2/#propdef-font-size), [ED](https://drafts.csswg.org/css2/#propdef-font-size), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-size), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-size)
background-color | 88.97% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/colors.html#propdef-background-color), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background-color), [ED](https://drafts.csswg.org/css2/#propdef-background-color), [ED](https://drafts.csswg.org/css2/#propdef-background-color), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background-color)
margin-top | 88.06% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-margin-top), [ED](https://drafts.csswg.org/css-box-3/#propdef-margin-top), [ED](https://drafts.csswg.org/css-box-4/#propdef-margin-top), [ED](https://drafts.csswg.org/css2/#propdef-margin-top), [ED](https://drafts.csswg.org/css2/#propdef-margin-top), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-margin-top), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-margin-top)
text-align | 87.88% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/text.html#propdef-text-align), [ED](https://drafts.csswg.org/css-text-3/#propdef-text-align), [ED](https://drafts.csswg.org/css-text-4/#propdef-text-align), [ED](https://drafts.csswg.org/css2/#propdef-text-align), [ED](https://drafts.csswg.org/css2/#propdef-text-align), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-text-align), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-align)
font-family | 87.64% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#propdef-font-family), [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-family), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-family), [ED](https://drafts.csswg.org/css2/#propdef-font-family), [ED](https://drafts.csswg.org/css2/#propdef-font-family), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-family), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-family)
font-weight | 87.51% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#propdef-font-weight), [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-weight), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-weight), [ED](https://drafts.csswg.org/css2/#propdef-font-weight), [ED](https://drafts.csswg.org/css2/#propdef-font-weight), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-weight), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-weight)
overflow | 87.04% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#propdef-overflow), [ED](https://drafts.csswg.org/css-overflow-3/#propdef-overflow), [ED](https://drafts.csswg.org/css2/#propdef-overflow), [ED](https://drafts.csswg.org/css2/#propdef-overflow), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-overflow)
background | 86.97% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/colors.html#propdef-background), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background), [ED](https://drafts.csswg.org/css2/#propdef-background), [ED](https://drafts.csswg.org/css2/#propdef-background), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background)
opacity | 86.27% | ✅ | [ED](https://drafts.csswg.org/css-color-3/#opacity), [ED](https://drafts.csswg.org/css-color-4/#propdef-opacity), [REC](https://www.w3.org/TR/2022/REC-css-color-3-20220118/#opacity), [CRD](https://www.w3.org/TR/2024/CRD-css-color-4-20240213/#propdef-opacity)
line-height | 85.89% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#propdef-line-height), [ED](https://drafts.csswg.org/css-inline-3/#propdef-line-height), [ED](https://drafts.csswg.org/css2/#propdef-line-height), [ED](https://drafts.csswg.org/css2/#propdef-line-height), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-line-height)
border-radius | 85.41% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-radius), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-radius)
box-sizing | 85.28% | ✅ | [ED](https://drafts.csswg.org/css-sizing-3/#propdef-box-sizing), [ED](https://drafts.csswg.org/css-ui-3/#propdef-box-sizing), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-box-sizing), [WD](https://www.w3.org/TR/2021/WD-css-sizing-3-20211217/#propdef-box-sizing)
z-index | 85.09% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-z-index), [ED](https://drafts.csswg.org/css2/#propdef-z-index), [ED](https://drafts.csswg.org/css2/#propdef-z-index)
cursor | 83.95% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/ui.html#propdef-cursor), [ED](https://drafts.csswg.org/css-ui-3/#propdef-cursor), [ED](https://drafts.csswg.org/css-ui-4/#propdef-cursor), [ED](https://drafts.csswg.org/css2/#propdef-cursor), [ED](https://drafts.csswg.org/css2/#propdef-cursor), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-cursor), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-cursor)
text-decoration | 83.55% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/text.html#propdef-text-decoration), [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-decoration), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration), [ED](https://drafts.csswg.org/css2/#propdef-text-decoration), [ED](https://drafts.csswg.org/css2/#propdef-text-decoration), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-decoration), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-decoration)
margin-bottom | 83.22% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-margin-bottom), [ED](https://drafts.csswg.org/css-box-3/#propdef-margin-bottom), [ED](https://drafts.csswg.org/css-box-4/#propdef-margin-bottom), [ED](https://drafts.csswg.org/css2/#propdef-margin-bottom), [ED](https://drafts.csswg.org/css2/#propdef-margin-bottom), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-margin-bottom), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-margin-bottom)
right | 83.02% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-right), [ED](https://drafts.csswg.org/css-position-3/#propdef-right), [ED](https://drafts.csswg.org/css2/#propdef-right), [ED](https://drafts.csswg.org/css2/#propdef-right), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-right)
margin-left | 82.94% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-margin-left), [ED](https://drafts.csswg.org/css-box-3/#propdef-margin-left), [ED](https://drafts.csswg.org/css-box-4/#propdef-margin-left), [ED](https://drafts.csswg.org/css2/#propdef-margin-left), [ED](https://drafts.csswg.org/css2/#propdef-margin-left), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-margin-left), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-margin-left)
transform | 82.75% | ✅ | [ED](https://drafts.csswg.org/css-transforms/#propdef-transform), [CR](https://www.w3.org/TR/2019/CR-css-transforms-1-20190214/#propdef-transform)
margin-right | 82.62% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-margin-right), [ED](https://drafts.csswg.org/css-box-3/#propdef-margin-right), [ED](https://drafts.csswg.org/css-box-4/#propdef-margin-right), [ED](https://drafts.csswg.org/css2/#propdef-margin-right), [ED](https://drafts.csswg.org/css2/#propdef-margin-right), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-margin-right), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-margin-right)
max-width | 82.37% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#propdef-max-width), [ED](https://drafts.csswg.org/css-sizing-3/#propdef-max-width), [ED](https://drafts.csswg.org/css2/#propdef-max-width), [ED](https://drafts.csswg.org/css2/#propdef-max-width), [WD](https://www.w3.org/TR/2021/WD-css-sizing-3-20211217/#propdef-max-width)
vertical-align | 81.54% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#propdef-vertical-align), [ED](https://drafts.csswg.org/css-inline-3/#propdef-vertical-align), [ED](https://drafts.csswg.org/css2/#propdef-vertical-align), [ED](https://drafts.csswg.org/css2/#propdef-vertical-align), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-vertical-align)
bottom | 81.16% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-bottom), [ED](https://drafts.csswg.org/css-position-3/#propdef-bottom), [ED](https://drafts.csswg.org/css2/#propdef-bottom), [ED](https://drafts.csswg.org/css2/#propdef-bottom), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-bottom)
content | 80.55% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/generate.html#propdef-content), [ED](https://drafts.csswg.org/css-content-3/#propdef-content), [ED](https://drafts.csswg.org/css2/#propdef-content), [ED](https://drafts.csswg.org/css2/#propdef-content), [WD](https://www.w3.org/TR/2019/WD-css-content-3-20190802/#propdef-content)
box-shadow | 80.50% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-box-shadow), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-box-shadow)
white-space | 80.44% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/text.html#propdef-white-space), [ED](https://drafts.csswg.org/css-text-3/#propdef-white-space), [ED](https://drafts.csswg.org/css-text-4/#propdef-white-space), [ED](https://drafts.csswg.org/css2/#propdef-white-space), [ED](https://drafts.csswg.org/css2/#propdef-white-space), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-white-space), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-white-space)
padding-left | 80.22% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-padding-left), [ED](https://drafts.csswg.org/css-box-3/#propdef-padding-left), [ED](https://drafts.csswg.org/css-box-4/#propdef-padding-left), [ED](https://drafts.csswg.org/css2/#propdef-padding-left), [ED](https://drafts.csswg.org/css2/#propdef-padding-left), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-padding-left), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-padding-left)
padding-top | 79.85% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-padding-top), [ED](https://drafts.csswg.org/css-box-3/#propdef-padding-top), [ED](https://drafts.csswg.org/css-box-4/#propdef-padding-top), [ED](https://drafts.csswg.org/css2/#propdef-padding-top), [ED](https://drafts.csswg.org/css2/#propdef-padding-top), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-padding-top), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-padding-top)
transition | 79.43% | ✅ | [ED](https://drafts.csswg.org/css-transitions/#propdef-transition), [WD](https://www.w3.org/TR/2018/WD-css-transitions-1-20181011/#propdef-transition)
min-height | 78.92% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#propdef-min-height), [ED](https://drafts.csswg.org/css-sizing-3/#propdef-min-height), [ED](https://drafts.csswg.org/css2/#propdef-min-height), [ED](https://drafts.csswg.org/css2/#propdef-min-height), [WD](https://www.w3.org/TR/2021/WD-css-sizing-3-20211217/#propdef-min-height)
font-style | 78.68% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#propdef-font-style), [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-style), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-style), [ED](https://drafts.csswg.org/css2/#propdef-font-style), [ED](https://drafts.csswg.org/css2/#propdef-font-style), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-style), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-style)
padding-right | 78.37% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-padding-right), [ED](https://drafts.csswg.org/css-box-3/#propdef-padding-right), [ED](https://drafts.csswg.org/css-box-4/#propdef-padding-right), [ED](https://drafts.csswg.org/css2/#propdef-padding-right), [ED](https://drafts.csswg.org/css2/#propdef-padding-right), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-padding-right), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-padding-right)
padding-bottom | 78.12% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-padding-bottom), [ED](https://drafts.csswg.org/css-box-3/#propdef-padding-bottom), [ED](https://drafts.csswg.org/css-box-4/#propdef-padding-bottom), [ED](https://drafts.csswg.org/css2/#propdef-padding-bottom), [ED](https://drafts.csswg.org/css2/#propdef-padding-bottom), [REC](https://www.w3.org/TR/2024/REC-css-box-3-20240411/#propdef-padding-bottom), [WD](https://www.w3.org/TR/2024/WD-css-box-4-20240401/#propdef-padding-bottom)
align-items | 77.44% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-align-items), [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-align-items), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-align-items), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-align-items)
float | 77.16% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-float), [ED](https://drafts.csswg.org/css-page-floats/#propdef-float), [ED](https://drafts.csswg.org/css2/#propdef-float), [ED](https://drafts.csswg.org/css2/#propdef-float), [FPWD](https://www.w3.org/TR/2015/WD-css-page-floats-3-20150915/#propdef-float)
justify-content | 77.12% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-justify-content), [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-justify-content), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-justify-content), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-justify-content)
background-image | 76.95% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/colors.html#propdef-background-image), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background-image), [ED](https://drafts.csswg.org/css2/#propdef-background-image), [ED](https://drafts.csswg.org/css2/#propdef-background-image), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background-image)
min-width | 76.90% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#propdef-min-width), [ED](https://drafts.csswg.org/css-sizing-3/#propdef-min-width), [ED](https://drafts.csswg.org/css2/#propdef-min-width), [ED](https://drafts.csswg.org/css2/#propdef-min-width), [WD](https://www.w3.org/TR/2021/WD-css-sizing-3-20211217/#propdef-min-width)
outline | 76.82% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/ui.html#propdef-outline), [ED](https://drafts.csswg.org/css-ui-3/#propdef-outline), [ED](https://drafts.csswg.org/css-ui-4/#propdef-outline), [ED](https://drafts.csswg.org/css2/#propdef-outline), [ED](https://drafts.csswg.org/css2/#propdef-outline), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-outline), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-outline)
border-bottom | 75.54% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-bottom), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-bottom), [ED](https://drafts.csswg.org/css2/#propdef-border-bottom), [ED](https://drafts.csswg.org/css2/#propdef-border-bottom), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-bottom)
border-color | 75.21% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-color), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-color), [ED](https://drafts.csswg.org/css2/#propdef-border-color), [ED](https://drafts.csswg.org/css2/#propdef-border-color), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-color)
background-position | 74.98% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/colors.html#propdef-background-position), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background-position), [ED](https://drafts.csswg.org/css2/#propdef-background-position), [ED](https://drafts.csswg.org/css2/#propdef-background-position), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background-position)
visibility | 74.73% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#propdef-visibility), [ED](https://drafts.csswg.org/css-display/#propdef-visibility), [ED](https://drafts.csswg.org/css2/#propdef-visibility), [ED](https://drafts.csswg.org/css2/#propdef-visibility), [CR](https://www.w3.org/TR/2023/CR-css-display-3-20230330/#propdef-visibility)
border-top | 72.43% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-top), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-top), [ED](https://drafts.csswg.org/css2/#propdef-border-top), [ED](https://drafts.csswg.org/css2/#propdef-border-top), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-top)
max-height | 72.32% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visudet.html#propdef-max-height), [ED](https://drafts.csswg.org/css-sizing-3/#propdef-max-height), [ED](https://drafts.csswg.org/css2/#propdef-max-height), [ED](https://drafts.csswg.org/css2/#propdef-max-height), [WD](https://www.w3.org/TR/2021/WD-css-sizing-3-20211217/#propdef-max-height)
background-size | 72.27% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background-size), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background-size)
text-transform | 72.17% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/text.html#propdef-text-transform), [ED](https://drafts.csswg.org/css-text-3/#propdef-text-transform), [ED](https://drafts.csswg.org/css-text-4/#propdef-text-transform), [ED](https://drafts.csswg.org/css2/#propdef-text-transform), [ED](https://drafts.csswg.org/css2/#propdef-text-transform), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-text-transform), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-transform)
flex-direction | 72.06% | ✅ | [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-flex-direction), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-flex-direction)
src | 71.96% | ❌ | N/A
background-repeat | 71.29% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/colors.html#propdef-background-repeat), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background-repeat), [ED](https://drafts.csswg.org/css2/#propdef-background-repeat), [ED](https://drafts.csswg.org/css2/#propdef-background-repeat), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background-repeat)
list-style | 67.61% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/generate.html#propdef-list-style), [ED](https://drafts.csswg.org/css-lists-3/#propdef-list-style), [ED](https://drafts.csswg.org/css2/#propdef-list-style), [ED](https://drafts.csswg.org/css2/#propdef-list-style), [WD](https://www.w3.org/TR/2020/WD-css-lists-3-20201117/#propdef-list-style)
flex-wrap | 67.06% | ✅ | [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-flex-wrap), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-flex-wrap)
pointer-events | 66.82% | ✅ | [ED](https://drafts.csswg.org/css-ui-4/#propdef-pointer-events)
overflow-y | 66.62% | ✅ | [ED](https://drafts.csswg.org/css-overflow-3/#propdef-overflow-y), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-overflow-y)
animation | 66.46% | ✅ | [ED](https://drafts.csswg.org/css-animations/#propdef-animation), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation)
flex | 65.55% | ✅ | [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-flex), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-flex)
clear | 65.30% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-clear), [ED](https://drafts.csswg.org/css-page-floats/#propdef-clear), [ED](https://drafts.csswg.org/css2/#propdef-clear), [ED](https://drafts.csswg.org/css2/#propdef-clear), [FPWD](https://www.w3.org/TR/2015/WD-css-page-floats-3-20150915/#propdef-clear)
letter-spacing | 65.26% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/text.html#propdef-letter-spacing), [ED](https://drafts.csswg.org/css-text-3/#propdef-letter-spacing), [ED](https://drafts.csswg.org/css-text-4/#propdef-letter-spacing), [ED](https://drafts.csswg.org/css2/#propdef-letter-spacing), [ED](https://drafts.csswg.org/css2/#propdef-letter-spacing), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-letter-spacing), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-letter-spacing)
border-width | 65.03% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-width), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-width), [ED](https://drafts.csswg.org/css2/#propdef-border-width), [ED](https://drafts.csswg.org/css2/#propdef-border-width), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-width)
text-overflow | 64.90% | 🧪 | [ED](https://drafts.csswg.org/css-overflow-3/#propdef-text-overflow), [ED](https://drafts.csswg.org/css-overflow-4/#propdef-text-overflow), [ED](https://drafts.csswg.org/css-ui-3/#propdef-text-overflow), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-text-overflow), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-text-overflow), [WD](https://www.w3.org/TR/2023/WD-css-overflow-4-20230321/#propdef-text-overflow)
font | 64.55% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#propdef-font), [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font), [ED](https://drafts.csswg.org/css2/#propdef-font), [ED](https://drafts.csswg.org/css2/#propdef-font), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font)
user-select | 64.32% | ❌ | [ED](https://drafts.csswg.org/css-ui-4/#propdef-user-select), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-user-select)
overflow-x | 63.06% | ✅ | [ED](https://drafts.csswg.org/css-overflow-3/#propdef-overflow-x), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-overflow-x)
border-left | 62.97% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-left), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-left), [ED](https://drafts.csswg.org/css2/#propdef-border-left), [ED](https://drafts.csswg.org/css2/#propdef-border-left), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-left)
border-right | 61.50% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-right), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-right), [ED](https://drafts.csswg.org/css2/#propdef-border-right), [ED](https://drafts.csswg.org/css2/#propdef-border-right), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-right)
variable | 61.36% | ❌ | N/A
fill | 60.77% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-fill), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-fill)
border-style | 60.09% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-style), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-style), [ED](https://drafts.csswg.org/css2/#propdef-border-style), [ED](https://drafts.csswg.org/css2/#propdef-border-style), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-style)
flex-grow | 56.55% | ✅ | [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-flex-grow), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-flex-grow)
flex-shrink | 55.71% | ✅ | [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-flex-shrink), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-flex-shrink)
word-wrap | 54.90% | ✅ | [ED](https://drafts.csswg.org/css-text-3/#propdef-word-wrap), [ED](https://drafts.csswg.org/css-text-4/#propdef-word-wrap), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-word-wrap), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-word-wrap)
word-wrap | 54.90% | ✅ | [ED](https://drafts.csswg.org/css-text-3/#propdef-word-wrap), [ED](https://drafts.csswg.org/css-text-4/#propdef-word-wrap), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-word-wrap), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-word-wrap)
word-break | 54.22% | ✅ | [ED](https://drafts.csswg.org/css-text-3/#propdef-word-break), [ED](https://drafts.csswg.org/css-text-4/#propdef-word-break), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-word-break), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-word-break)
border-top-right-radius | 52.25% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-top-right-radius), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-top-right-radius)
border-top-left-radius | 51.73% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-top-left-radius), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-top-left-radius)
transform-origin | 50.85% | ✅ | [ED](https://drafts.csswg.org/css-transforms/#propdef-transform-origin), [CR](https://www.w3.org/TR/2019/CR-css-transforms-1-20190214/#propdef-transform-origin)
font-display | 50.10% | ❌ | N/A
gap | 49.82% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-gap), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-gap)
border-bottom-left-radius | 49.43% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-bottom-left-radius), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-bottom-left-radius)
clip | 49.34% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visufx.html#propdef-clip), [ED](https://drafts.csswg.org/css2/#propdef-clip), [ED](https://drafts.csswg.org/css2/#propdef-clip), [ED](https://drafts.fxtf.org/css-masking-1/#propdef-clip), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-clip)
border-bottom-right-radius | 49.22% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-bottom-right-radius), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-bottom-right-radius)
align-self | 48.44% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-align-self), [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-align-self), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-align-self), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-align-self)
border-collapse | 47.09% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#propdef-border-collapse), [ED](https://drafts.csswg.org/css-tables-3/#propdef-border-collapse), [ED](https://drafts.csswg.org/css2/#propdef-border-collapse), [ED](https://drafts.csswg.org/css2/#propdef-border-collapse), [WD](https://www.w3.org/TR/2019/WD-css-tables-3-20190727/#propdef-border-collapse)
list-style-type | 46.65% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/generate.html#propdef-list-style-type), [ED](https://drafts.csswg.org/css-lists-3/#propdef-list-style-type), [ED](https://drafts.csswg.org/css2/#propdef-list-style-type), [ED](https://drafts.csswg.org/css2/#propdef-list-style-type), [WD](https://www.w3.org/TR/2020/WD-css-lists-3-20201117/#propdef-list-style-type)
object-fit | 45.77% | ✅ | [ED](https://drafts.csswg.org/css-images-3/#propdef-object-fit), [ED](https://drafts.csswg.org/css-images-4/#propdef-object-fit), [CRD](https://www.w3.org/TR/2023/CRD-css-images-3-20231218/#propdef-object-fit), [WD](https://www.w3.org/TR/2023/WD-css-images-4-20230217/#propdef-object-fit)
text-shadow | 45.04% | ✅ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-shadow), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-shadow), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-shadow), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-shadow)
animation-timing-function | 44.94% | ✅ | [ED](https://drafts.csswg.org/css-animations/#propdef-animation-timing-function), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation-timing-function)
unicode-range | 43.68% | ❌ | N/A
filter | 43.35% | ✅ | [ED](https://drafts.fxtf.org/filter-effects-1/#propdef-filter), [WD](https://www.w3.org/TR/2018/WD-filter-effects-1-20181218/#propdef-filter)
animation-duration | 43.20% | ✅ | [ED](https://drafts.csswg.org/css-animations-2/#propdef-animation-duration), [ED](https://drafts.csswg.org/css-animations/#propdef-animation-duration), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation-duration), [WD](https://www.w3.org/TR/2023/WD-css-animations-2-20230602/#propdef-animation-duration)
direction | 42.80% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-direction), [ED](https://drafts.csswg.org/css-writing-modes-3/#propdef-direction), [ED](https://drafts.csswg.org/css-writing-modes-4/#propdef-direction), [ED](https://drafts.csswg.org/css2/#propdef-direction), [ED](https://drafts.csswg.org/css2/#propdef-direction), [CR](https://www.w3.org/TR/2019/CR-css-writing-modes-4-20190730/#propdef-direction), [REC](https://www.w3.org/TR/2019/REC-css-writing-modes-3-20191210/#propdef-direction)
appearance | 42.54% | ❌ | [ED](https://drafts.csswg.org/css-ui-4/#propdef-appearance), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-appearance)
animation-name | 42.54% | ✅ | [ED](https://drafts.csswg.org/css-animations/#propdef-animation-name), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation-name)
border-top-color | 41.43% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-top-color), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-top-color), [ED](https://drafts.csswg.org/css2/#propdef-border-top-color), [ED](https://drafts.csswg.org/css2/#propdef-border-top-color), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-top-color)
border-bottom-color | 41.12% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-bottom-color), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-bottom-color), [ED](https://drafts.csswg.org/css2/#propdef-border-bottom-color), [ED](https://drafts.csswg.org/css2/#propdef-border-bottom-color), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-bottom-color)
flex-basis | 41.01% | ✅ | [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-flex-basis), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-flex-basis)
touch-action | 40.82% | ❌ | N/A
stroke-width | 40.70% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-stroke-width), [ED](https://svgwg.org/specs/strokes/#StrokeWidthProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-strokes-20150409/#StrokeWidthProperty), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-stroke-width)
outline-offset | 40.47% | ✅ | [ED](https://drafts.csswg.org/css-ui-3/#propdef-outline-offset), [ED](https://drafts.csswg.org/css-ui-4/#propdef-outline-offset), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-outline-offset), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-outline-offset)
transition-duration | 39.03% | ✅ | [ED](https://drafts.csswg.org/css-transitions/#propdef-transition-duration), [WD](https://www.w3.org/TR/2018/WD-css-transitions-1-20181011/#propdef-transition-duration)
stroke | 38.71% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-stroke), [ED](https://svgwg.org/specs/strokes/#StrokeProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-strokes-20150409/#StrokeProperty), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-stroke)
background-clip | 38.04% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background-clip), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background-clip)
text-indent | 37.55% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/text.html#propdef-text-indent), [ED](https://drafts.csswg.org/css-text-3/#propdef-text-indent), [ED](https://drafts.csswg.org/css-text-4/#propdef-text-indent), [ED](https://drafts.csswg.org/css2/#propdef-text-indent), [ED](https://drafts.csswg.org/css2/#propdef-text-indent), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-text-indent), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-indent)
transition-property | 37.49% | ✅ | [ED](https://drafts.csswg.org/css-transitions/#propdef-transition-property), [WD](https://www.w3.org/TR/2018/WD-css-transitions-1-20181011/#propdef-transition-property)
order | 37.35% | ✅ | [ED](https://drafts.csswg.org/css-display/#propdef-order), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-order), [CR](https://www.w3.org/TR/2023/CR-css-display-3-20230330/#propdef-order)
grid-template-columns | 35.77% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-template-columns), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-template-columns), [ED](https://drafts.csswg.org/css-template/#grid-template-columns), [NOTE](https://www.w3.org/TR/2015/NOTE-css-template-3-20150326/#grid-template-columns), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-template-columns), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-template-columns)
animation-delay | 35.39% | ✅ | [ED](https://drafts.csswg.org/css-animations/#propdef-animation-delay), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation-delay)
transition-timing-function | 35.33% | ✅ | [ED](https://drafts.csswg.org/css-transitions/#propdef-transition-timing-function), [WD](https://www.w3.org/TR/2018/WD-css-transitions-1-20181011/#propdef-transition-timing-function)
align-content | 35.11% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-align-content), [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-align-content), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-align-content), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-align-content)
scrollbar-width | 34.31% | ❌ | [ED](https://drafts.csswg.org/css-scrollbars/#propdef-scrollbar-width), [CR](https://www.w3.org/TR/2021/CR-css-scrollbars-1-20211209/#propdef-scrollbar-width)
border-left-color | 34.11% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-left-color), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-left-color), [ED](https://drafts.csswg.org/css2/#propdef-border-left-color), [ED](https://drafts.csswg.org/css2/#propdef-border-left-color), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-left-color)
text-rendering | 33.60% | ✅ | N/A
border-spacing | 33.36% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#propdef-border-spacing), [ED](https://drafts.csswg.org/css-tables-3/#propdef-border-spacing), [ED](https://drafts.csswg.org/css2/#propdef-border-spacing), [ED](https://drafts.csswg.org/css2/#propdef-border-spacing), [WD](https://www.w3.org/TR/2019/WD-css-tables-3-20190727/#propdef-border-spacing)
resize | 32.84% | ❌ | [ED](https://drafts.csswg.org/css-ui-3/#propdef-resize), [ED](https://drafts.csswg.org/css-ui-4/#propdef-resize), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-resize), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-resize)
will-change | 32.77% | ❌ | [ED](https://drafts.csswg.org/css-will-change/#propdef-will-change), [CRD](https://www.w3.org/TR/2022/CRD-css-will-change-1-20220505/#propdef-will-change)
border-right-color | 32.73% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-right-color), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-right-color), [ED](https://drafts.csswg.org/css2/#propdef-border-right-color), [ED](https://drafts.csswg.org/css2/#propdef-border-right-color), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-right-color)
clip-path | 32.41% | ✅ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-clip-path), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-clip-path)
overflow-wrap | 31.60% | ✅ | [ED](https://drafts.csswg.org/css-text-3/#propdef-overflow-wrap), [ED](https://drafts.csswg.org/css-text-4/#propdef-overflow-wrap), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-overflow-wrap), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-overflow-wrap)
animation-iteration-count | 30.89% | ✅ | [ED](https://drafts.csswg.org/css-animations/#propdef-animation-iteration-count), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation-iteration-count)
animation-fill-mode | 30.23% | ✅ | [ED](https://drafts.csswg.org/css-animations/#propdef-animation-fill-mode), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation-fill-mode)
flex-flow | 29.75% | ✅ | [ED](https://drafts.csswg.org/css-flexbox-1/#propdef-flex-flow), [CR](https://www.w3.org/TR/2018/CR-css-flexbox-1-20181119/#propdef-flex-flow)
transition-delay | 29.48% | ✅ | [ED](https://drafts.csswg.org/css-transitions/#propdef-transition-delay), [WD](https://www.w3.org/TR/2018/WD-css-transitions-1-20181011/#propdef-transition-delay)
font-variant | 28.29% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/fonts.html#propdef-font-variant), [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-variant), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variant), [ED](https://drafts.csswg.org/css2/#propdef-font-variant), [ED](https://drafts.csswg.org/css2/#propdef-font-variant), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-variant), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variant)
column-gap | 28.24% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-column-gap), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-column-gap)
zoom | 27.34% | ❌ | [ED](https://drafts.csswg.org/css-device-adapt/#propdef-zoom), [ED](https://drafts.csswg.org/css-viewport/#propdef-zoom)
border-bottom-width | 26.79% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-bottom-width), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-bottom-width), [ED](https://drafts.csswg.org/css2/#propdef-border-bottom-width), [ED](https://drafts.csswg.org/css2/#propdef-border-bottom-width), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-bottom-width)
inset | 26.51% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-inset), [ED](https://drafts.csswg.org/css-position-3/#propdef-inset), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-inset), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-inset)
stroke-dashoffset | 26.50% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-stroke-dashoffset), [ED](https://svgwg.org/specs/strokes/#StrokeDashoffsetProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-strokes-20150409/#StrokeDashoffsetProperty), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-stroke-dashoffset)
outline-width | 26.45% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/ui.html#propdef-outline-width), [ED](https://drafts.csswg.org/css-ui-3/#propdef-outline-width), [ED](https://drafts.csswg.org/css-ui-4/#propdef-outline-width), [ED](https://drafts.csswg.org/css2/#propdef-outline-width), [ED](https://drafts.csswg.org/css2/#propdef-outline-width), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-outline-width), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-outline-width)
border-left-width | 25.06% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-left-width), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-left-width), [ED](https://drafts.csswg.org/css2/#propdef-border-left-width), [ED](https://drafts.csswg.org/css2/#propdef-border-left-width), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-left-width)
border-right-width | 25.05% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-right-width), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-right-width), [ED](https://drafts.csswg.org/css2/#propdef-border-right-width), [ED](https://drafts.csswg.org/css2/#propdef-border-right-width), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-right-width)
outline-color | 24.87% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/ui.html#propdef-outline-color), [ED](https://drafts.csswg.org/css-ui-3/#propdef-outline-color), [ED](https://drafts.csswg.org/css-ui-4/#propdef-outline-color), [ED](https://drafts.csswg.org/css2/#propdef-outline-color), [ED](https://drafts.csswg.org/css2/#propdef-outline-color), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-outline-color), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-outline-color)
stroke-dasharray | 24.63% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-stroke-dasharray), [ED](https://svgwg.org/specs/strokes/#StrokeDasharrayProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-strokes-20150409/#StrokeDasharrayProperty), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-stroke-dasharray)
aspect-ratio | 24.35% | ✅ | [ED](https://drafts.csswg.org/css-sizing-4/#propdef-aspect-ratio), [WD](https://www.w3.org/TR/2021/WD-css-sizing-4-20210520/#propdef-aspect-ratio)
border-top-width | 24.16% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-top-width), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-top-width), [ED](https://drafts.csswg.org/css2/#propdef-border-top-width), [ED](https://drafts.csswg.org/css2/#propdef-border-top-width), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-top-width)
backdrop-filter | 23.59% | ❌ | N/A
text-size-adjust | 21.43% | ❌ | N/A
grid-template-rows | 20.48% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-template-rows), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-template-rows), [ED](https://drafts.csswg.org/css-template/#grid-template-rows), [NOTE](https://www.w3.org/TR/2015/NOTE-css-template-3-20150326/#grid-template-rows), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-template-rows), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-template-rows)
row-gap | 20.30% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-row-gap), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-row-gap)
backface-visibility | 19.28% | ✅ | [ED](https://drafts.csswg.org/css-transforms-2/#propdef-backface-visibility), [ED](https://drafts.csswg.org/css-transforms-2/#propdef-backface-visibility), [WD](https://www.w3.org/TR/2021/WD-css-transforms-2-20211109/#propdef-backface-visibility)
grid-column | 19.01% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-column), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-column), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-column), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-column)
margin-inline-start | 18.84% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-margin-inline-start), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-margin-inline-start)
font-feature-settings | 18.60% | ❌ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-feature-settings), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-feature-settings), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-feature-settings), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-feature-settings)
outline-style | 18.50% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/ui.html#propdef-outline-style), [ED](https://drafts.csswg.org/css-ui-3/#propdef-outline-style), [ED](https://drafts.csswg.org/css-ui-4/#propdef-outline-style), [ED](https://drafts.csswg.org/css2/#propdef-outline-style), [ED](https://drafts.csswg.org/css2/#propdef-outline-style), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-outline-style), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-outline-style)
grid-gap | 18.37% | ✅ | N/A
grid-gap | 18.37% | ✅ | N/A
table-layout | 18.22% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#propdef-table-layout), [ED](https://drafts.csswg.org/css-tables-3/#propdef-table-layout), [ED](https://drafts.csswg.org/css2/#propdef-table-layout), [ED](https://drafts.csswg.org/css2/#propdef-table-layout), [WD](https://www.w3.org/TR/2019/WD-css-tables-3-20190727/#propdef-table-layout)
contain | 18.15% | ❌ | [ED](https://drafts.csswg.org/css-contain-1/#propdef-contain), [ED](https://drafts.csswg.org/css-contain-2/#propdef-contain), [WD](https://www.w3.org/TR/2022/WD-css-contain-2-20220917/#propdef-contain), [REC](https://www.w3.org/TR/2024/REC-css-contain-1-20240625/#propdef-contain)
grid-area | 17.72% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-area), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-area), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-area), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-area)
animation-direction | 17.26% | ✅ | [ED](https://drafts.csswg.org/css-animations/#propdef-animation-direction), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation-direction)
text-decoration-line | 17.08% | ✅ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-decoration-line), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration-line), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-decoration-line), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-decoration-line)
border-bottom-style | 17.07% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-bottom-style), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-bottom-style), [ED](https://drafts.csswg.org/css2/#propdef-border-bottom-style), [ED](https://drafts.csswg.org/css2/#propdef-border-bottom-style), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-bottom-style)
forced-color-adjust | 16.60% | ❌ | [ED](https://drafts.csswg.org/css-color-adjust-1/#propdef-forced-color-adjust), [CRD](https://www.w3.org/TR/2022/CRD-css-color-adjust-1-20220614/#propdef-forced-color-adjust)
color-scheme | 16.23% | ❌ | [ED](https://drafts.csswg.org/css-color-adjust-1/#propdef-color-scheme), [CRD](https://www.w3.org/TR/2022/CRD-css-color-adjust-1-20220614/#propdef-color-scheme)
object-position | 16.18% | ✅ | [ED](https://drafts.csswg.org/css-images-3/#propdef-object-position), [CRD](https://www.w3.org/TR/2023/CRD-css-images-3-20231218/#propdef-object-position)
margin-inline-end | 16.04% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-margin-inline-end), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-margin-inline-end)
scroll-boundary-behavior | 16.01% | ❌ | N/A
scroll-boundary-behavior | 16.01% | ❌ | N/A
mask-image | 15.79% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-image), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-image)
mask | 15.25% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask)
padding-inline-start | 15.20% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-padding-inline-start), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-padding-inline-start)
padding-inline | 14.74% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-padding-inline), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-padding-inline)
scroll-behavior | 14.51% | ❌ | [ED](https://drafts.csswg.org/css-overflow-3/#propdef-scroll-behavior), [WD](https://www.w3.org/TR/2016/WD-cssom-view-1-20160317/#propdef-scroll-behavior), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-scroll-behavior)
font-stretch | 14.27% | ✅ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-stretch), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-stretch)
grid-row | 14.07% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-row), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-row), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-row), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-row)
word-spacing | 14.06% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/text.html#propdef-word-spacing), [ED](https://drafts.csswg.org/css-text-3/#propdef-word-spacing), [ED](https://drafts.csswg.org/css-text-4/#propdef-word-spacing), [ED](https://drafts.csswg.org/css2/#propdef-word-spacing), [ED](https://drafts.csswg.org/css2/#propdef-word-spacing), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-word-spacing), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-word-spacing)
text-wrap | 13.98% | ❌ | [ED](https://drafts.csswg.org/css-text-4/#propdef-text-wrap), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-wrap)
justify-items | 13.92% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-justify-items), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-justify-items)
scroll-snap-type | 13.47% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-snap-type), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-snap-type)
unicode-bidi | 13.13% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/visuren.html#propdef-unicode-bidi), [ED](https://drafts.csswg.org/css-writing-modes-3/#propdef-unicode-bidi), [ED](https://drafts.csswg.org/css-writing-modes-4/#propdef-unicode-bidi), [ED](https://drafts.csswg.org/css2/#propdef-unicode-bidi), [ED](https://drafts.csswg.org/css2/#propdef-unicode-bidi), [CR](https://www.w3.org/TR/2019/CR-css-writing-modes-4-20190730/#propdef-unicode-bidi), [REC](https://www.w3.org/TR/2019/REC-css-writing-modes-3-20191210/#propdef-unicode-bidi)
padding-block | 12.96% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-padding-block), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-padding-block)
background-position-x | 12.88% | ✅ | N/A
padding-inline-end | 12.67% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-padding-inline-end), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-padding-inline-end)
text-decoration-color | 12.66% | ✅ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-decoration-color), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration-color), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-decoration-color), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-decoration-color)
caret-color | 12.56% | ❌ | [ED](https://drafts.csswg.org/css-ui-3/#propdef-caret-color), [ED](https://drafts.csswg.org/css-ui-4/#propdef-caret-color), [REC](https://www.w3.org/TR/2018/REC-css-ui-3-20180621/#propdef-caret-color), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-caret-color)
border-top-style | 12.34% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-top-style), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-top-style), [ED](https://drafts.csswg.org/css2/#propdef-border-top-style), [ED](https://drafts.csswg.org/css2/#propdef-border-top-style), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-top-style)
margin-block-start | 12.22% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-margin-block-start), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-margin-block-start)
justify-self | 12.19% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-justify-self), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-justify-self)
transform-style | 11.88% | ✅ | [ED](https://drafts.csswg.org/css-transforms-2/#propdef-transform-style), [ED](https://drafts.csswg.org/css-transforms-2/#propdef-transform-style), [WD](https://www.w3.org/TR/2021/WD-css-transforms-2-20211109/#propdef-transform-style)
speak | 11.53% | ❌ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/aural.html#propdef-speak), [ED](https://drafts.csswg.org/css-speech-1/#propdef-speak), [CRD](https://www.w3.org/TR/2023/CRD-css-speech-1-20230214/#propdef-speak)
font-variation-settings | 11.44% | ❌ | [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variation-settings), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variation-settings)
animation-play-state | 11.28% | ✅ | [ED](https://drafts.csswg.org/css-animations/#propdef-animation-play-state), [WD](https://www.w3.org/TR/2023/WD-css-animations-1-20230302/#propdef-animation-play-state)
margin-block-end | 11.26% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-margin-block-end), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-margin-block-end)
inset-inline-start | 11.14% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-inset-inline-start), [ED](https://drafts.csswg.org/css-position-3/#propdef-inset-inline-start), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-inset-inline-start), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-inset-inline-start)
grid-template-areas | 10.72% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-template-areas), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-template-areas), [ED](https://drafts.csswg.org/css-template/#grid-template-areas), [NOTE](https://www.w3.org/TR/2015/NOTE-css-template-3-20150326/#grid-template-areas), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-template-areas), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-template-areas)
fill-opacity | 10.70% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-fill-opacity), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-fill-opacity)
counter-increment | 10.69% | 🧪 | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/generate.html#propdef-counter-increment), [ED](https://drafts.csswg.org/css-lists-3/#propdef-counter-increment), [ED](https://drafts.csswg.org/css2/#propdef-counter-increment), [ED](https://drafts.csswg.org/css2/#propdef-counter-increment), [WD](https://www.w3.org/TR/2020/WD-css-lists-3-20201117/#propdef-counter-increment)
grid-auto-flow | 10.65% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-auto-flow), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-auto-flow), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-auto-flow), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-auto-flow)
margin-inline | 10.49% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-margin-inline), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-margin-inline)
hyphens | 10.12% | ❌ | [ED](https://drafts.csswg.org/css-text-3/#propdef-hyphens), [ED](https://drafts.csswg.org/css-text-4/#propdef-hyphens), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-hyphens), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-hyphens)
list-style-position | 10.11% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/generate.html#propdef-list-style-position), [ED](https://drafts.csswg.org/css-lists-3/#propdef-list-style-position), [ED](https://drafts.csswg.org/css2/#propdef-list-style-position), [ED](https://drafts.csswg.org/css2/#propdef-list-style-position), [WD](https://www.w3.org/TR/2020/WD-css-lists-3-20201117/#propdef-list-style-position)
isolation | 10.10% | ❌ | [ED](https://drafts.fxtf.org/compositing-1/#propdef-isolation), [CRD](https://www.w3.org/TR/2024/CRD-compositing-1-20240321/#propdef-isolation)
margin-block | 9.73% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-margin-block), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-margin-block)
grid-column-gap | 9.65% | ✅ | N/A
grid-column-gap | 9.65% | ✅ | N/A
perspective | 9.62% | ✅ | [ED](https://drafts.csswg.org/css-transforms-2/#propdef-perspective), [ED](https://drafts.csswg.org/css-transforms-2/#propdef-perspective), [WD](https://www.w3.org/TR/2021/WD-css-transforms-2-20211109/#propdef-perspective)
all | 9.56% | ✅ | [ED](https://drafts.csswg.org/css-cascade-3/#propdef-all), [ED](https://drafts.csswg.org/css-cascade-4/#propdef-all), [ED](https://drafts.csswg.org/css-cascade-5/#propdef-all), [REC](https://www.w3.org/TR/2021/REC-css-cascade-3-20210211/#propdef-all), [CR](https://www.w3.org/TR/2022/CR-css-cascade-4-20220113/#propdef-all), [CR](https://www.w3.org/TR/2022/CR-css-cascade-5-20220113/#propdef-all)
counter-reset | 9.44% | 🧪 | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/generate.html#propdef-counter-reset), [ED](https://drafts.csswg.org/css-lists-3/#propdef-counter-reset), [ED](https://drafts.csswg.org/css2/#propdef-counter-reset), [ED](https://drafts.csswg.org/css2/#propdef-counter-reset), [WD](https://www.w3.org/TR/2020/WD-css-lists-3-20201117/#propdef-counter-reset)
inset-inline-end | 9.34% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-inset-inline-end), [ED](https://drafts.csswg.org/css-position-3/#propdef-inset-inline-end), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-inset-inline-end), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-inset-inline-end)
border-start-start-radius | 9.02% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-start-start-radius), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-start-start-radius)
border-end-end-radius | 9.01% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-end-end-radius), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-end-end-radius)
border-end-start-radius | 8.95% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-end-start-radius), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-end-start-radius)
border-start-end-radius | 8.88% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-start-end-radius), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-start-end-radius)
scrollbar-color | 8.71% | ❌ | [ED](https://drafts.csswg.org/css-scrollbars/#propdef-scrollbar-color), [CR](https://www.w3.org/TR/2021/CR-css-scrollbars-1-20211209/#propdef-scrollbar-color)
inline-size | 8.58% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-inline-size), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-inline-size)
inset-block-start | 8.54% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-inset-block-start), [ED](https://drafts.csswg.org/css-position-3/#propdef-inset-block-start), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-inset-block-start), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-inset-block-start)
border-left-style | 8.49% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-left-style), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-left-style), [ED](https://drafts.csswg.org/css2/#propdef-border-left-style), [ED](https://drafts.csswg.org/css2/#propdef-border-left-style), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-left-style)
stroke-linecap | 8.47% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-stroke-linecap), [ED](https://svgwg.org/specs/strokes/#StrokeLinecapProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-strokes-20150409/#StrokeLinecapProperty), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-stroke-linecap)
block-size | 8.44% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-block-size), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-block-size)
tab-size | 8.40% | ❌ | [ED](https://drafts.csswg.org/css-text-3/#propdef-tab-size), [ED](https://drafts.csswg.org/css-text-4/#propdef-tab-size), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-tab-size), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-tab-size)
min-inline-size | 8.26% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-min-inline-size), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-min-inline-size)
background-attachment | 8.20% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/colors.html#propdef-background-attachment), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background-attachment), [ED](https://drafts.csswg.org/css2/#propdef-background-attachment), [ED](https://drafts.csswg.org/css2/#propdef-background-attachment), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background-attachment)
scroll-snap-align | 8.17% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-snap-align), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-snap-align)
quotes | 8.14% | 🧪 | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/generate.html#propdef-quotes), [ED](https://drafts.csswg.org/css-content-3/#propdef-quotes), [ED](https://drafts.csswg.org/css2/#propdef-quotes), [ED](https://drafts.csswg.org/css2/#propdef-quotes), [WD](https://www.w3.org/TR/2019/WD-css-content-3-20190802/#propdef-quotes)
background-blend-mode | 8.14% | ❌ | [ED](https://drafts.fxtf.org/compositing-1/#propdef-background-blend-mode), [CRD](https://www.w3.org/TR/2024/CRD-compositing-1-20240321/#propdef-background-blend-mode)
mask-size | 8.11% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-size), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-size)
padding-block-end | 8.09% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-padding-block-end), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-padding-block-end)
padding-block-start | 8.08% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-padding-block-start), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-padding-block-start)
min-block-size | 7.93% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-min-block-size), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-min-block-size)
background-position-y | 7.91% | ✅ | N/A
max-inline-size | 7.83% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-max-inline-size), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-max-inline-size)
max-block-size | 7.77% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-max-block-size), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-max-block-size)
image-rendering | 7.74% | ✅ | [ED](https://drafts.csswg.org/css-images-3/#propdef-image-rendering), [CRD](https://www.w3.org/TR/2023/CRD-css-images-3-20231218/#propdef-image-rendering)
border-right-style | 7.73% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/box.html#propdef-border-right-style), [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-right-style), [ED](https://drafts.csswg.org/css2/#propdef-border-right-style), [ED](https://drafts.csswg.org/css2/#propdef-border-right-style), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-right-style)
mask-position | 7.71% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-position), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-position)
stroke-miterlimit | 7.68% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-stroke-miterlimit), [ED](https://svgwg.org/specs/strokes/#StrokeMiterlimitProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-strokes-20150409/#StrokeMiterlimitProperty), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-stroke-miterlimit)
mix-blend-mode | 7.45% | ✅ | [ED](https://drafts.fxtf.org/compositing-1/#propdef-mix-blend-mode), [CRD](https://www.w3.org/TR/2024/CRD-compositing-1-20240321/#propdef-mix-blend-mode)
inset-inline | 7.45% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-inset-inline), [ED](https://drafts.csswg.org/css-position-3/#propdef-inset-inline), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-inset-inline), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-inset-inline)
border-inline-start | 7.44% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-start), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-start)
border-inline-end | 7.35% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-end), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-end)
background-origin | 7.27% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-background-origin), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-background-origin)
border-block-end | 6.95% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-end), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-end)
inset-block | 6.89% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-inset-block), [ED](https://drafts.csswg.org/css-position-3/#propdef-inset-block), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-inset-block), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-inset-block)
border-block-start | 6.76% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-start), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-start)
container | 6.71% | ❌ | [ED](https://drafts.csswg.org/css-conditional-5/#propdef-container), [WD](https://www.w3.org/TR/2022/WD-css-contain-3-20220818/#propdef-container)
border-block-end-width | 6.66% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-end-width), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-end-width)
size | 6.64% | ❌ | N/A
mask-composite | 6.59% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-composite), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-composite)
inset-block-end | 6.59% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-inset-block-end), [ED](https://drafts.csswg.org/css-position-3/#propdef-inset-block-end), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-inset-block-end), [WD](https://www.w3.org/TR/2023/WD-css-position-3-20230403/#propdef-inset-block-end)
border-block-end-color | 6.41% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-end-color), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-end-color)
scroll-padding | 6.36% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding)
mask-repeat | 6.32% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-repeat), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-repeat)
grid-row-start | 6.16% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-row-start), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-row-start), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-row-start), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-row-start)
column-count | 6.13% | 🧪 | [ED](https://drafts.csswg.org/css-multicol/#propdef-column-count), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-column-count)
stroke-opacity | 6.08% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-stroke-opacity), [ED](https://svgwg.org/specs/strokes/#StrokeOpacityProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-strokes-20150409/#StrokeOpacityProperty), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-stroke-opacity)
place-content | 6.08% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-place-content), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-place-content)
grid-auto-rows | 5.91% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-auto-rows), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-auto-rows), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-auto-rows), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-auto-rows)
overflow-anchor | 5.87% | ❌ | [ED](https://drafts.csswg.org/css-scroll-anchoring/#propdef-overflow-anchor), [WD](https://www.w3.org/TR/2020/WD-css-scroll-anchoring-1-20201111/#propdef-overflow-anchor)
grid-column-start | 5.85% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-column-start), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-column-start), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-column-start), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-column-start)
scroll-boundary-behavior-y | 5.80% | ❌ | N/A
scroll-boundary-behavior-y | 5.80% | ❌ | N/A
caption-side | 5.77% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#propdef-caption-side), [ED](https://drafts.csswg.org/css-tables-3/#propdef-caption-side), [ED](https://drafts.csswg.org/css2/#propdef-caption-side), [ED](https://drafts.csswg.org/css2/#propdef-caption-side), [WD](https://www.w3.org/TR/2019/WD-css-tables-3-20190727/#propdef-caption-side)
font-variant-ligatures | 5.73% | ❌ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-variant-ligatures), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variant-ligatures), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-variant-ligatures), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variant-ligatures)
border-image | 5.67% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-image), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-image)
grid-row-gap | 5.43% | ✅ | N/A
grid-row-gap | 5.43% | ✅ | N/A
page-break-inside | 5.37% | ❌ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/page.html#propdef-page-break-inside), [ED](https://drafts.csswg.org/css2/#propdef-page-break-inside), [ED](https://drafts.csswg.org/css2/#propdef-page-break-inside)
place-items | 5.33% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-place-items), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-place-items)
grid-auto-columns | 5.20% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-auto-columns), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-auto-columns), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-auto-columns), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-auto-columns)
text-decoration-thickness | 5.15% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration-thickness), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-decoration-thickness)
text-underline-offset | 5.05% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-underline-offset), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-underline-offset)
grid-column-end | 4.73% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-column-end), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-column-end), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-column-end), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-column-end)
r | 4.67% | ❌ | N/A
stop-opacity | 4.62% | ❌ | N/A
intrinsic-size | 4.60% | ❌ | N/A
intrinsic-size | 4.60% | ❌ | N/A
content-visibility | 4.53% | ❌ | [ED](https://drafts.csswg.org/css-contain-2/#propdef-content-visibility), [WD](https://www.w3.org/TR/2022/WD-css-contain-2-20220917/#propdef-content-visibility)
container-type | 4.48% | ❌ | [ED](https://drafts.csswg.org/css-conditional-5/#propdef-container-type), [WD](https://www.w3.org/TR/2022/WD-css-contain-3-20220818/#propdef-container-type)
list-style-image | 4.47% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/generate.html#propdef-list-style-image), [ED](https://drafts.csswg.org/css-lists-3/#propdef-list-style-image), [ED](https://drafts.csswg.org/css2/#propdef-list-style-image), [ED](https://drafts.csswg.org/css2/#propdef-list-style-image), [WD](https://www.w3.org/TR/2020/WD-css-lists-3-20201117/#propdef-list-style-image)
text-decoration-skip | 4.44% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration-skip), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-decoration-skip)
text-decoration-skip | 4.44% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration-skip), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-decoration-skip)
line-break | 4.44% | ❌ | [ED](https://drafts.csswg.org/css-text-3/#propdef-line-break), [ED](https://drafts.csswg.org/css-text-4/#propdef-line-break), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-line-break), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-line-break)
line-break | 4.44% | ❌ | [ED](https://drafts.csswg.org/css-text-3/#propdef-line-break), [ED](https://drafts.csswg.org/css-text-4/#propdef-line-break), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-line-break), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-line-break)
scale | 4.43% | ✅ | [ED](https://drafts.csswg.org/css-transforms-2/#propdef-scale), [ED](https://drafts.csswg.org/css-transforms-2/#propdef-scale), [WD](https://www.w3.org/TR/2021/WD-css-transforms-2-20211109/#propdef-scale)
cx | 4.43% | ❌ | N/A
cy | 4.37% | ❌ | N/A
grid-row-end | 4.31% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-row-end), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-row-end), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-row-end), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-row-end)
font-variant-numeric | 3.80% | ❌ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-variant-numeric), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variant-numeric), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-variant-numeric), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variant-numeric)
page-break-after | 3.73% | ❌ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/page.html#propdef-page-break-after), [ED](https://drafts.csswg.org/css2/#propdef-page-break-after), [ED](https://drafts.csswg.org/css2/#propdef-page-break-after)
y | 3.63% | ❌ | N/A
stroke-linejoin | 3.56% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-stroke-linejoin), [ED](https://svgwg.org/specs/strokes/#StrokeLinejoinProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-strokes-20150409/#StrokeLinejoinProperty), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-stroke-linejoin)
scrollbar-gutter | 3.51% | ❌ | [ED](https://drafts.csswg.org/css-overflow-3/#propdef-scrollbar-gutter), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-scrollbar-gutter)
x | 3.50% | ❌ | N/A
perspective-origin | 3.48% | ✅ | [ED](https://drafts.csswg.org/css-transforms-2/#propdef-perspective-origin), [ED](https://drafts.csswg.org/css-transforms-2/#propdef-perspective-origin), [WD](https://www.w3.org/TR/2021/WD-css-transforms-2-20211109/#propdef-perspective-origin)
fill-rule | 3.45% | ❌ | [ED](https://drafts.fxtf.org/fill-stroke/#propdef-fill-rule), [FPWD](https://www.w3.org/TR/2017/WD-fill-stroke-3-20170413/#propdef-fill-rule)
scroll-snap-stop | 3.35% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-snap-stop), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-snap-stop)
empty-cells | 3.31% | ✅ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/tables.html#propdef-empty-cells), [ED](https://drafts.csswg.org/css-tables-3/#propdef-empty-cells), [ED](https://drafts.csswg.org/css2/#propdef-empty-cells), [ED](https://drafts.csswg.org/css2/#propdef-empty-cells), [WD](https://www.w3.org/TR/2019/WD-css-tables-3-20190727/#propdef-empty-cells)
rotate | 3.15% | ✅ | [ED](https://drafts.csswg.org/css-transforms-2/#propdef-rotate), [ED](https://drafts.csswg.org/css-transforms-2/#propdef-rotate), [WD](https://www.w3.org/TR/2021/WD-css-transforms-2-20211109/#propdef-rotate)
columns | 3.02% | 🧪 | [ED](https://drafts.csswg.org/css-multicol/#propdef-columns), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-columns)
column-width | 3.01% | 🧪 | [ED](https://drafts.csswg.org/css-multicol/#propdef-column-width), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-column-width)
break-inside | 2.99% | ❌ | [ED](https://drafts.csswg.org/css-break-4/#propdef-break-inside), [ED](https://drafts.csswg.org/css-break/#propdef-break-inside), [WD](https://www.w3.org/TR/2014/WD-css-regions-1-20141009/#propdef-break-inside), [CR](https://www.w3.org/TR/2018/CR-css-break-3-20181204/#propdef-break-inside), [FPWD](https://www.w3.org/TR/2018/WD-css-break-4-20181218/#propdef-break-inside)
text-decoration-style | 2.94% | ✅ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-decoration-style), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration-style), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-decoration-style), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-decoration-style)
text-decoration-skip-ink | 2.81% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-decoration-skip-ink), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-decoration-skip-ink)
orphans | 2.78% | ❌ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/page.html#propdef-orphans), [ED](https://drafts.csswg.org/css-break-4/#propdef-orphans), [ED](https://drafts.csswg.org/css-break/#propdef-orphans), [ED](https://drafts.csswg.org/css2/#propdef-orphans), [ED](https://drafts.csswg.org/css2/#propdef-orphans), [CR](https://www.w3.org/TR/2018/CR-css-break-3-20181204/#propdef-orphans), [FPWD](https://www.w3.org/TR/2018/WD-css-break-4-20181218/#propdef-orphans)
widows | 2.74% | ❌ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/page.html#propdef-widows), [ED](https://drafts.csswg.org/css-break-4/#propdef-widows), [ED](https://drafts.csswg.org/css-break/#propdef-widows), [ED](https://drafts.csswg.org/css2/#propdef-widows), [ED](https://drafts.csswg.org/css2/#propdef-widows), [CR](https://www.w3.org/TR/2018/CR-css-break-3-20181204/#propdef-widows), [FPWD](https://www.w3.org/TR/2018/WD-css-break-4-20181218/#propdef-widows)
scroll-snap-margin-top | 2.71% | ❌ | N/A
scroll-snap-margin-top | 2.71% | ❌ | N/A
text-align-last | 2.59% | ✅ | [ED](https://drafts.csswg.org/css-text-3/#propdef-text-align-last), [ED](https://drafts.csswg.org/css-text-4/#propdef-text-align-last), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-text-align-last), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-align-last)
column-rule | 2.40% | ❌ | [ED](https://drafts.csswg.org/css-multicol/#propdef-column-rule), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-column-rule)
box-decoration-break | 2.19% | ❌ | [ED](https://drafts.csswg.org/css-break-4/#propdef-box-decoration-break), [ED](https://drafts.csswg.org/css-break/#propdef-box-decoration-break), [CR](https://www.w3.org/TR/2018/CR-css-break-3-20181204/#propdef-box-decoration-break), [FPWD](https://www.w3.org/TR/2018/WD-css-break-4-20181218/#propdef-box-decoration-break)
border-inline-end-width | 2.17% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-end-width), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-end-width)
scroll-boundary-behavior-x | 2.02% | ❌ | N/A
scroll-boundary-behavior-x | 2.02% | ❌ | N/A
scroll-padding-top | 2.01% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-top), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-top)
stop-color | 1.96% | ❌ | N/A
mask-mode | 1.96% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-mode), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-mode)
shape-outside | 1.91% | ❌ | [ED](https://drafts.csswg.org/css-shapes/#propdef-shape-outside), [CRD](https://www.w3.org/TR/2022/CRD-css-shapes-1-20221115/#propdef-shape-outside)
column-fill | 1.88% | ❌ | [ED](https://drafts.csswg.org/css-multicol/#propdef-column-fill), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-column-fill)
scroll-snap-margin | 1.87% | ❌ | N/A
scroll-snap-margin | 1.87% | ❌ | N/A
flood-opacity | 1.84% | ❌ | [ED](https://drafts.fxtf.org/filter-effects-1/#propdef-flood-opacity), [WD](https://www.w3.org/TR/2018/WD-filter-effects-1-20181218/#propdef-flood-opacity)
page-break-before | 1.82% | ❌ | [REC](http://www.w3.org/TR/2011/REC-CSS2-20110607/page.html#propdef-page-break-before), [ED](https://drafts.csswg.org/css2/#propdef-page-break-before), [ED](https://drafts.csswg.org/css2/#propdef-page-break-before)
border-inline-start-width | 1.75% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-start-width), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-start-width)
writing-mode | 1.71% | 🧪 | [ED](https://drafts.csswg.org/css-writing-modes-3/#propdef-writing-mode), [ED](https://drafts.csswg.org/css-writing-modes-4/#propdef-writing-mode), [CR](https://www.w3.org/TR/2019/CR-css-writing-modes-4-20190730/#propdef-writing-mode), [REC](https://www.w3.org/TR/2019/REC-css-writing-modes-3-20191210/#propdef-writing-mode)
grid-template | 1.71% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid-template), [ED](https://drafts.csswg.org/css-grid/#propdef-grid-template), [ED](https://drafts.csswg.org/css-template/#grid-template0), [NOTE](https://www.w3.org/TR/2015/NOTE-css-template-3-20150326/#grid-template0), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid-template), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid-template)
place-self | 1.62% | ✅ | [ED](https://drafts.csswg.org/css-align/#propdef-place-self), [WD](https://www.w3.org/TR/2023/WD-css-align-3-20230217/#propdef-place-self)
container-name | 1.60% | ❌ | [ED](https://drafts.csswg.org/css-conditional-5/#propdef-container-name), [WD](https://www.w3.org/TR/2022/WD-css-contain-3-20220818/#propdef-container-name)
size-adjust | 1.60% | ❌ | N/A
ascent-override | 1.52% | ❌ | N/A
mask-type | 1.52% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-type), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-type)
text-underline-position | 1.46% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-underline-position), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-underline-position), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-underline-position), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-underline-position)
translate | 1.46% | ✅ | [ED](https://drafts.csswg.org/css-transforms-2/#propdef-translate), [ED](https://drafts.csswg.org/css-transforms-2/#propdef-translate), [WD](https://www.w3.org/TR/2021/WD-css-transforms-2-20211109/#propdef-translate)
font-size-adjust | 1.41% | ❌ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-size-adjust), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-size-adjust), [ED](https://drafts.csswg.org/css-fonts-5/#propdef-font-size-adjust), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-size-adjust), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-size-adjust), [WD](https://www.w3.org/TR/2024/WD-css-fonts-5-20240206/#propdef-font-size-adjust)
column-rule-color | 1.41% | ❌ | [ED](https://drafts.csswg.org/css-multicol/#propdef-column-rule-color), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-column-rule-color)
font-kerning | 1.37% | ❌ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-kerning), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-kerning), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-kerning), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-kerning)
column-rule-style | 1.36% | ❌ | [ED](https://drafts.csswg.org/css-multicol/#propdef-column-rule-style), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-column-rule-style)
text-anchor | 1.30% | ❌ | N/A
transform-box | 1.28% | ❌ | [ED](https://drafts.csswg.org/css-transforms/#propdef-transform-box), [CR](https://www.w3.org/TR/2019/CR-css-transforms-1-20190214/#propdef-transform-box)
descent-override | 1.27% | ❌ | N/A
border-image-slice | 1.27% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-image-slice), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-image-slice)
border-block-start-width | 1.27% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-start-width), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-start-width)
accent-color | 1.25% | ❌ | [ED](https://drafts.csswg.org/css-ui-4/#propdef-accent-color), [WD](https://www.w3.org/TR/2021/WD-css-ui-4-20210316/#propdef-accent-color)
border-image-source | 1.24% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-image-source), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-image-source)
border-inline-start-color | 1.19% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-start-color), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-start-color)
clip-rule | 1.16% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-clip-rule), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-clip-rule)
font-synthesis | 1.16% | ❌ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-synthesis), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-synthesis), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-synthesis), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-synthesis)
scroll-padding-left | 1.07% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-left), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-left)
syntax | 1.03% | ❌ | N/A
overscroll-behavior-inline | 1.02% | ❌ | [ED](https://drafts.csswg.org/css-overscroll-1/#propdef-overscroll-behavior-inline), [FPWD](https://www.w3.org/TR/2019/WD-css-overscroll-1-20190606/#propdef-overscroll-behavior-inline)
overscroll-behavior-inline | 1.02% | ❌ | [ED](https://drafts.csswg.org/css-overscroll-1/#propdef-overscroll-behavior-inline), [FPWD](https://www.w3.org/TR/2019/WD-css-overscroll-1-20190606/#propdef-overscroll-behavior-inline)
overscroll-behavior-block | 1.01% | ❌ | [ED](https://drafts.csswg.org/css-overscroll-1/#propdef-overscroll-behavior-block), [FPWD](https://www.w3.org/TR/2019/WD-css-overscroll-1-20190606/#propdef-overscroll-behavior-block)
overscroll-behavior-block | 1.01% | ❌ | [ED](https://drafts.csswg.org/css-overscroll-1/#propdef-overscroll-behavior-block), [FPWD](https://www.w3.org/TR/2019/WD-css-overscroll-1-20190606/#propdef-overscroll-behavior-block)
line-gap-override | 1.01% | ❌ | N/A
shape-rendering | 0.93% | ❌ | N/A
border-block-start-style | 0.91% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-start-style), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-start-style)
border-image-width | 0.88% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-image-width), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-image-width)
border-inline-end-color | 0.87% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-end-color), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-end-color)
border-block-start-color | 0.86% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-start-color), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-start-color)
column-span | 0.83% | 🧪 | [ED](https://drafts.csswg.org/css-multicol/#propdef-column-span), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-column-span)
overflow-clip-margin | 0.77% | ❌ | [ED](https://drafts.csswg.org/css-overflow-3/#propdef-overflow-clip-margin), [ED](https://drafts.csswg.org/css-overflow-4/#propdef-overflow-clip-margin), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-overflow-clip-margin), [WD](https://www.w3.org/TR/2023/WD-css-overflow-4-20230321/#propdef-overflow-clip-margin)
break-after | 0.77% | ❌ | [ED](https://drafts.csswg.org/css-break-4/#propdef-break-after), [ED](https://drafts.csswg.org/css-break/#propdef-break-after), [WD](https://www.w3.org/TR/2014/WD-css-regions-1-20141009/#propdef-break-after), [CR](https://www.w3.org/TR/2018/CR-css-break-3-20181204/#propdef-break-after), [FPWD](https://www.w3.org/TR/2018/WD-css-break-4-20181218/#propdef-break-after)
border-block-end-style | 0.76% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-end-style), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-end-style)
vector-effect | 0.74% | ❌ | N/A
dominant-baseline | 0.73% | ❌ | [ED](https://drafts.csswg.org/css-inline-3/#propdef-dominant-baseline), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-dominant-baseline)
border-block | 0.73% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block)
border-image-repeat | 0.73% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-image-repeat), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-image-repeat)
font-variant-caps | 0.69% | ✅ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-variant-caps), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variant-caps), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-variant-caps), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variant-caps)
break-before | 0.65% | ❌ | [ED](https://drafts.csswg.org/css-break-4/#propdef-break-before), [ED](https://drafts.csswg.org/css-break/#propdef-break-before), [WD](https://www.w3.org/TR/2014/WD-css-regions-1-20141009/#propdef-break-before), [CR](https://www.w3.org/TR/2018/CR-css-break-3-20181204/#propdef-break-before), [FPWD](https://www.w3.org/TR/2018/WD-css-break-4-20181218/#propdef-break-before)
background-repeat-x (obsolete) | 0.64% | ❌ | N/A
background-repeat-x (obsolete) | 0.64% | ❌ | N/A
scroll-padding-inline | 0.63% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-inline), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-inline)
font-optical-sizing | 0.63% | ❌ | [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-optical-sizing), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-optical-sizing)
scroll-padding-block | 0.57% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-block), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-block)
scroll-padding-block-end | 0.56% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-block-end), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-block-end)
border-inline-start-style | 0.55% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-start-style), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-start-style)
animation-timeline | 0.54% | ❌ | [ED](https://drafts.csswg.org/css-animations-2/#propdef-animation-timeline), [WD](https://www.w3.org/TR/2023/WD-css-animations-2-20230602/#propdef-animation-timeline)
text-orientation | 0.52% | ❌ | [ED](https://drafts.csswg.org/css-writing-modes-3/#propdef-text-orientation), [ED](https://drafts.csswg.org/css-writing-modes-4/#propdef-text-orientation), [CR](https://www.w3.org/TR/2019/CR-css-writing-modes-4-20190730/#propdef-text-orientation), [REC](https://www.w3.org/TR/2019/REC-css-writing-modes-3-20191210/#propdef-text-orientation)
font-variant-east-asian | 0.52% | ❌ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-variant-east-asian), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variant-east-asian), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-variant-east-asian), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variant-east-asian)
border-image-outset | 0.51% | ✅ | [ED](https://drafts.csswg.org/css-backgrounds/#propdef-border-image-outset), [CRD](https://www.w3.org/TR/2024/CRD-css-backgrounds-3-20240311/#propdef-border-image-outset)
border-inline-end-style | 0.51% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-end-style), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-end-style)
grid | 0.51% | 🧪 | [ED](https://drafts.csswg.org/css-grid-2/#propdef-grid), [ED](https://drafts.csswg.org/css-grid/#propdef-grid), [ED](https://drafts.csswg.org/css-template/#grid), [NOTE](https://www.w3.org/TR/2015/NOTE-css-template-3-20150326/#grid), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-1-20201218/#propdef-grid), [CRD](https://www.w3.org/TR/2020/CRD-css-grid-2-20201218/#propdef-grid)
paint-order | 0.48% | ❌ | N/A
view-transition-name | 0.46% | ❌ | [ED](https://drafts.csswg.org/css-view-transitions-1/#propdef-view-transition-name), [CRD](https://www.w3.org/TR/2024/CRD-css-view-transitions-1-20240328/#propdef-view-transition-name)
view-transition-name | 0.46% | ❌ | [ED](https://drafts.csswg.org/css-view-transitions-1/#propdef-view-transition-name), [CRD](https://www.w3.org/TR/2024/CRD-css-view-transitions-1-20240328/#propdef-view-transition-name)
alignment-baseline | 0.46% | ❌ | [ED](https://drafts.csswg.org/css-inline-3/#propdef-alignment-baseline), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-alignment-baseline)
scroll-snap-margin-bottom | 0.45% | ❌ | N/A
scroll-snap-margin-bottom | 0.45% | ❌ | N/A
column-rule-width | 0.44% | ❌ | [ED](https://drafts.csswg.org/css-multicol/#propdef-column-rule-width), [CR](https://www.w3.org/TR/2024/CR-css-multicol-1-20240516/#propdef-column-rule-width)
shape-margin | 0.43% | ❌ | [ED](https://drafts.csswg.org/css-shapes/#propdef-shape-margin), [CRD](https://www.w3.org/TR/2022/CRD-css-shapes-1-20221115/#propdef-shape-margin)
baseline-shift | 0.41% | ❌ | [ED](https://drafts.csswg.org/css-inline-3/#propdef-baseline-shift), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-baseline-shift)
scroll-padding-bottom | 0.41% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-bottom), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-bottom)
shape-image-threshold | 0.40% | ❌ | [ED](https://drafts.csswg.org/css-shapes/#propdef-shape-image-threshold), [CRD](https://www.w3.org/TR/2022/CRD-css-shapes-1-20221115/#propdef-shape-image-threshold)
rx | 0.39% | ❌ | N/A
system | 0.39% | ❌ | N/A
suffix | 0.39% | ❌ | N/A
symbols | 0.39% | ❌ | N/A
flood-color | 0.36% | ❌ | [ED](https://drafts.fxtf.org/filter-effects-1/#propdef-flood-color), [WD](https://www.w3.org/TR/2018/WD-filter-effects-1-20181218/#propdef-flood-color)
counter-set | 0.36% | ❌ | [ED](https://drafts.csswg.org/css-lists-3/#propdef-counter-set), [WD](https://www.w3.org/TR/2020/WD-css-lists-3-20201117/#propdef-counter-set)
d | 0.36% | ❌ | N/A
text-emphasis-color | 0.34% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-emphasis-color), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-emphasis-color), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-emphasis-color), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-emphasis-color)
page-orientation | 0.31% | ❌ | N/A
border-inline-width | 0.31% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-width), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-width)
animation-composition | 0.31% | ❌ | [ED](https://drafts.csswg.org/css-animations-2/#propdef-animation-composition), [WD](https://www.w3.org/TR/2023/WD-css-animations-2-20230602/#propdef-animation-composition)
border-block-width | 0.30% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-width), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-width)
font-variant-alternates | 0.29% | ❌ | [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variant-alternates), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variant-alternates)
text-combine-upright | 0.29% | ❌ | [ED](https://drafts.csswg.org/css-writing-modes-3/#propdef-text-combine-upright), [ED](https://drafts.csswg.org/css-writing-modes-4/#propdef-text-combine-upright), [CR](https://www.w3.org/TR/2019/CR-css-writing-modes-4-20190730/#propdef-text-combine-upright), [REC](https://www.w3.org/TR/2019/REC-css-writing-modes-3-20191210/#propdef-text-combine-upright)
mask-origin | 0.29% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-origin), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-origin)
text-spacing-trim | 0.28% | ❌ | [ED](https://drafts.csswg.org/css-text-4/#propdef-text-spacing-trim), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-spacing-trim)
font-variant-position | 0.28% | ❌ | [ED](https://drafts.csswg.org/css-fonts-3/#propdef-font-variant-position), [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variant-position), [REC](https://www.w3.org/TR/2018/REC-css-fonts-3-20180920/#propdef-font-variant-position), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variant-position)
offset | 0.27% | ❌ | [ED](https://drafts.fxtf.org/motion-1/#propdef-offset), [WD](https://www.w3.org/TR/2018/WD-motion-1-20181218/#propdef-offset)
color-interpolation-filters | 0.27% | ❌ | [ED](https://drafts.fxtf.org/filter-effects-1/#propdef-color-interpolation-filters), [WD](https://www.w3.org/TR/2018/WD-filter-effects-1-20181218/#propdef-color-interpolation-filters)
border-block-style | 0.26% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-style), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-style)
image-orientation-0 | 0.26% | ❌ | N/A
image-orientation-0 | 0.26% | ❌ | N/A
text-emphasis | 0.26% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-emphasis), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-emphasis), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-emphasis), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-emphasis)
lighting-color | 0.25% | ❌ | [ED](https://drafts.fxtf.org/filter-effects-1/#propdef-lighting-color), [WD](https://www.w3.org/TR/2018/WD-filter-effects-1-20181218/#propdef-lighting-color)
mask-clip | 0.25% | ❌ | [ED](https://drafts.fxtf.org/css-masking-1/#propdef-mask-clip), [CRD](https://www.w3.org/TR/2021/CRD-css-masking-1-20210805/#propdef-mask-clip)
buffered-rendering | 0.25% | ❌ | N/A
background-repeat-y (obsolete) | 0.25% | ❌ | N/A
background-repeat-y (obsolete) | 0.25% | ❌ | N/A
white-space-collapse | 0.24% | ✅ | [ED](https://drafts.csswg.org/css-text-4/#propdef-white-space-collapse), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-white-space-collapse)
ry | 0.24% | ❌ | N/A
scroll-padding-right | 0.24% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-right), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-right)
page | 0.24% | ❌ | [ED](https://drafts.csswg.org/css-page-3/#propdef-page), [WD](https://www.w3.org/TR/2023/WD-css-page-3-20230914/#propdef-page)
scroll-snap-margin-left | 0.24% | ❌ | N/A
scroll-snap-margin-left | 0.24% | ❌ | N/A
ruby-position | 0.24% | ❌ | [ED](https://drafts.csswg.org/css-ruby-1/#propdef-ruby-position), [WD](https://www.w3.org/TR/2022/WD-css-ruby-1-20221231/#propdef-ruby-position)
text-emphasis-position | 0.24% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-emphasis-position), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-emphasis-position), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-emphasis-position), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-emphasis-position)
border-inline | 0.23% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline)
hyphenate-character | 0.22% | ❌ | [ED](https://drafts.csswg.org/css-text-4/#propdef-hyphenate-character), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-hyphenate-character)
offset-distance | 0.22% | ❌ | [ED](https://drafts.fxtf.org/motion-1/#propdef-offset-distance), [WD](https://www.w3.org/TR/2018/WD-motion-1-20181218/#propdef-offset-distance)
marker-end | 0.21% | ❌ | [ED](https://svgwg.org/specs/markers/#MarkerEndProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-markers-20150409/#MarkerEndProperty)
color-interpolation | 0.21% | ❌ | N/A
color-rendering | 0.21% | ❌ | N/A
marker-start | 0.20% | ❌ | [ED](https://svgwg.org/specs/markers/#MarkerStartProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-markers-20150409/#MarkerStartProperty)
offset-rotate | 0.20% | ❌ | [ED](https://drafts.fxtf.org/motion-1/#propdef-offset-rotate), [WD](https://www.w3.org/TR/2018/WD-motion-1-20181218/#propdef-offset-rotate)
offset-path | 0.19% | ❌ | [ED](https://drafts.fxtf.org/motion-1/#propdef-offset-path), [WD](https://www.w3.org/TR/2018/WD-motion-1-20181218/#propdef-offset-path)
marker-mid | 0.19% | ❌ | [ED](https://svgwg.org/specs/markers/#MarkerMidProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-markers-20150409/#MarkerMidProperty)
app-region | 0.19% | ❌ | N/A
ruby-align | 0.19% | ❌ | [ED](https://drafts.csswg.org/css-ruby-1/#propdef-ruby-align), [WD](https://www.w3.org/TR/2022/WD-css-ruby-1-20221231/#propdef-ruby-align)
text-emphasis-style | 0.17% | ❌ | [ED](https://drafts.csswg.org/css-text-decor-3/#propdef-text-emphasis-style), [ED](https://drafts.csswg.org/css-text-decor-4/#propdef-text-emphasis-style), [CRD](https://www.w3.org/TR/2022/CRD-css-text-decor-3-20220505/#propdef-text-emphasis-style), [WD](https://www.w3.org/TR/2022/WD-css-text-decor-4-20220504/#propdef-text-emphasis-style)
intrinsic-height | 0.17% | ❌ | N/A
intrinsic-height | 0.17% | ❌ | N/A
view-timeline-name | 0.16% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-view-timeline-name), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-view-timeline-name)
animation-range | 0.16% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-animation-range), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-animation-range)
form-sizing | 0.16% | ❌ | N/A
form-sizing | 0.16% | ❌ | N/A
overscroll-behavior-inline | 0.16% | ❌ | [ED](https://drafts.csswg.org/css-overscroll-1/#propdef-overscroll-behavior-inline), [FPWD](https://www.w3.org/TR/2019/WD-css-overscroll-1-20190606/#propdef-overscroll-behavior-inline)
view-timeline-axis | 0.16% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-view-timeline-axis), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-view-timeline-axis)
transition-behavior | 0.15% | ✅ | [ED](https://drafts.csswg.org/css-transitions-2/#propdef-transition-behavior), [FPWD](https://www.w3.org/TR/2023/WD-css-transitions-2-20230905/#propdef-transition-behavior)
transition-behavior | 0.15% | ✅ | [ED](https://drafts.csswg.org/css-transitions-2/#propdef-transition-behavior), [FPWD](https://www.w3.org/TR/2023/WD-css-transitions-2-20230905/#propdef-transition-behavior)
scroll-snap-margin-right | 0.13% | ❌ | N/A
scroll-snap-margin-right | 0.13% | ❌ | N/A
scroll-padding-block-start | 0.12% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-block-start), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-block-start)
scroll-padding-inline-start | 0.12% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-inline-start), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-inline-start)
scroll-snap-margin-inline | 0.12% | ❌ | N/A
scroll-snap-margin-inline | 0.12% | ❌ | N/A
scroll-snap-margin-block-start | 0.10% | ❌ | N/A
scroll-snap-margin-block-start | 0.10% | ❌ | N/A
overscroll-behavior-block | 0.09% | ❌ | [ED](https://drafts.csswg.org/css-overscroll-1/#propdef-overscroll-behavior-block), [FPWD](https://www.w3.org/TR/2019/WD-css-overscroll-1-20190606/#propdef-overscroll-behavior-block)
scroll-snap-margin-block | 0.08% | ❌ | N/A
scroll-snap-margin-block | 0.08% | ❌ | N/A
intrinsic-block-size | 0.08% | ❌ | N/A
intrinsic-block-size | 0.08% | ❌ | N/A
scroll-snap-margin-inline-start | 0.08% | ❌ | N/A
scroll-snap-margin-inline-start | 0.08% | ❌ | N/A
initial-letter | 0.08% | ❌ | [ED](https://drafts.csswg.org/css-inline-3/#propdef-initial-letter), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-initial-letter)
intrinsic-inline-size | 0.08% | ❌ | N/A
intrinsic-inline-size | 0.08% | ❌ | N/A
scroll-padding-inline-end | 0.07% | ❌ | [ED](https://drafts.csswg.org/css-scroll-snap-1/#propdef-scroll-padding-inline-end), [CR](https://www.w3.org/TR/2021/CR-css-scroll-snap-1-20210311/#propdef-scroll-padding-inline-end)
scroll-snap-margin-block-end | 0.06% | ❌ | N/A
scroll-snap-margin-block-end | 0.06% | ❌ | N/A
scroll-snap-margin-inline-end | 0.06% | ❌ | N/A
scroll-snap-margin-inline-end | 0.06% | ❌ | N/A
hyphenate-limit-chars | 0.06% | ❌ | [ED](https://drafts.csswg.org/css-text-4/#propdef-hyphenate-limit-chars), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-hyphenate-limit-chars)
navigation-trigger | 0.06% | ❌ | N/A
navigation-trigger | 0.06% | ❌ | N/A
font-synthesis-weight | 0.05% | ❌ | [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-synthesis-weight), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-synthesis-weight)
border-inline-color | 0.05% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-color), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-color)
anchor-name | 0.04% | ❌ | [ED](https://drafts.csswg.org/css-anchor-position-1/#propdef-anchor-name), [WD](https://www.w3.org/TR/2024/WD-css-anchor-position-1-20240326/#propdef-anchor-name)
text-wrap-mode | 0.04% | ✅ | [ED](https://drafts.csswg.org/css-text-4/#propdef-text-wrap-mode), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-wrap-mode)
font-palette | 0.04% | ❌ | [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-palette), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-palette)
marker | 0.04% | ❌ | [ED](https://svgwg.org/specs/markers/#MarkerProperty), [FPWD](https://www.w3.org/TR/2015/WD-svg-markers-20150409/#MarkerProperty)
interpolate-size | 0.04% | ❌ | N/A
border-inline-style | 0.04% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-inline-style), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-inline-style)
animation-range-start | 0.04% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-animation-range-start), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-animation-range-start)
animation-range-end | 0.04% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-animation-range-end), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-animation-range-end)
position-anchor | 0.03% | ❌ | [ED](https://drafts.csswg.org/css-anchor-position-1/#propdef-position-anchor), [WD](https://www.w3.org/TR/2024/WD-css-anchor-position-1-20240326/#propdef-position-anchor)
intrinsic-width | 0.03% | ❌ | N/A
intrinsic-width | 0.03% | ❌ | N/A
border-block-color | 0.03% | ✅ | [ED](https://drafts.csswg.org/css-logical-1/#propdef-border-block-color), [WD](https://www.w3.org/TR/2018/WD-css-logical-1-20180827/#propdef-border-block-color)
view-transition-class | 0.03% | ❌ | [ED](https://drafts.csswg.org/css-view-transitions-2/#propdef-view-transition-class), [FPWD](https://www.w3.org/TR/2024/WD-css-view-transitions-2-20240516/#propdef-view-transition-class)
font-synthesis-style | 0.03% | ❌ | [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-synthesis-style), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-synthesis-style)
font-variant-emoji | 0.03% | ❌ | [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-variant-emoji), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-variant-emoji)
position-visibility | 0.03% | ❌ | [ED](https://drafts.csswg.org/css-anchor-position-1/#propdef-position-visibility)
overlay | 0.03% | ❌ | N/A
object-view-box | 0.03% | ❌ | N/A
scroll-timeline | 0.03% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-scroll-timeline), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-scroll-timeline)
offset-rotation | 0.03% | ❌ | N/A
offset-rotation | 0.03% | ❌ | N/A
baseline-source | 0.02% | ✅ | [ED](https://drafts.csswg.org/css-inline-3/#propdef-baseline-source), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-baseline-source)
timeline-scope | 0.02% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-timeline-scope), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-timeline-scope)
math-style | 0.02% | ❌ | N/A
position-try | 0.02% | ❌ | [ED](https://drafts.csswg.org/css-anchor-position-1/#propdef-position-try), [WD](https://www.w3.org/TR/2024/WD-css-anchor-position-1-20240326/#propdef-position-try)
math-depth | 0.02% | ❌ | N/A
position-area | 0.02% | ❌ | N/A
math-shift | 0.02% | ❌ | N/A
inset-area (obsolete) | 0.02% | ❌ | N/A
inset-area (obsolete) | 0.02% | ❌ | N/A
anchor-scope | 0.02% | ❌ | [ED](https://drafts.csswg.org/css-anchor-position-1/#propdef-anchor-scope), [WD](https://www.w3.org/TR/2024/WD-css-anchor-position-1-20240326/#propdef-anchor-scope)
position-try-order | 0.02% | ❌ | [ED](https://drafts.csswg.org/css-anchor-position-1/#propdef-position-try-order), [WD](https://www.w3.org/TR/2024/WD-css-anchor-position-1-20240326/#propdef-position-try-order)
text-wrap-style | 0.02% | ❌ | [ED](https://drafts.csswg.org/css-text-4/#propdef-text-wrap-style), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-wrap-style)
view-timeline | 0.02% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-view-timeline), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-view-timeline)
scroll-timeline-axis | 0.02% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-scroll-timeline-axis), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-scroll-timeline-axis)
offset-anchor | 0.02% | ❌ | [ED](https://drafts.fxtf.org/motion-1/#propdef-offset-anchor), [WD](https://www.w3.org/TR/2018/WD-motion-1-20181218/#propdef-offset-anchor)
scroll-timeline-name | 0.02% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-scroll-timeline-name), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-scroll-timeline-name)
position-try-fallbacks | 0.02% | ❌ | N/A
view-timeline-inset | 0.01% | ❌ | [ED](https://drafts.csswg.org/scroll-animations-1/#propdef-view-timeline-inset), [WD](https://www.w3.org/TR/2023/WD-scroll-animations-1-20230606/#propdef-view-timeline-inset)
offset-position | 0.01% | ❌ | [ED](https://drafts.fxtf.org/motion-1/#propdef-offset-position), [WD](https://www.w3.org/TR/2018/WD-motion-1-20181218/#propdef-offset-position)
font-synthesis-small-caps | 0.01% | ❌ | [ED](https://drafts.csswg.org/css-fonts-4/#propdef-font-synthesis-small-caps), [WD](https://www.w3.org/TR/2024/WD-css-fonts-4-20240201/#propdef-font-synthesis-small-caps)
position-try-options (obsolete) | 0.01% | ❌ | N/A
position-try-options (obsolete) | 0.01% | ❌ | N/A
range | 0.01% | ❌ | N/A
additive-symbols | 0.01% | ❌ | N/A
line-clamp | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-overflow-4/#propdef-line-clamp), [WD](https://www.w3.org/TR/2023/WD-css-overflow-4-20230321/#propdef-line-clamp)
prefix | 0.00% | ❌ | N/A
motion | 0.00% | ❌ | N/A
motion | 0.00% | ❌ | N/A
speak-as | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-speech-1/#propdef-speak-as), [CRD](https://www.w3.org/TR/2023/CRD-css-speech-1-20230214/#propdef-speak-as)
orientation | 0.00% | ❌ | N/A
base-palette | 0.00% | ❌ | N/A
pad | 0.00% | ❌ | N/A
mask-source-type | 0.00% | ❌ | N/A
motion-path | 0.00% | ❌ | N/A
motion-path | 0.00% | ❌ | N/A
motion-path | 0.00% | ❌ | N/A
motion-offset | 0.00% | ❌ | N/A
motion-offset | 0.00% | ❌ | N/A
motion-offset | 0.00% | ❌ | N/A
math-superscript-shift-style (obsolete) | 0.00% | ❌ | N/A
math-superscript-shift-style (obsolete) | 0.00% | ❌ | N/A
override-colors | 0.00% | ❌ | N/A
text-autospace | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-text-4/#propdef-text-autospace), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-autospace)
fallback | 0.00% | ❌ | N/A
scroll-start-target | 0.00% | ❌ | N/A
dynamic-range-limit | 0.00% | ❌ | N/A
reading-order-items | 0.00% | ❌ | N/A
reading-order-items | 0.00% | ❌ | N/A
scroll-markers | 0.00% | ❌ | N/A
scroll-markers | 0.00% | ❌ | N/A
view-transition-group | 0.00% | ❌ | N/A
text-box | 0.00% | ❌ | N/A
text-box-trim | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-inline-3/#propdef-text-box-trim), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-text-box-trim)
text-box-edge | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-inline-3/#propdef-text-box-edge), [WD](https://www.w3.org/TR/2023/WD-css-inline-3-20230401/#propdef-text-box-edge)
types | 0.00% | ❌ | N/A
text-justify | 0.00% | ✅ | [ED](https://drafts.csswg.org/css-text-3/#propdef-text-justify), [ED](https://drafts.csswg.org/css-text-4/#propdef-text-justify), [CRD](https://www.w3.org/TR/2023/CRD-css-text-3-20230903/#propdef-text-justify), [WD](https://www.w3.org/TR/2024/WD-css-text-4-20240529/#propdef-text-justify)
snap-height | 0.00% | ❌ | N/A
snap-height | 0.00% | ❌ | N/A
snap-height | 0.00% | ❌ | N/A
negative | 0.00% | ❌ | N/A
toggle-group (obsolete) | 0.00% | ❌ | N/A
toggle-group (obsolete) | 0.00% | ❌ | N/A
toggle-root (obsolete) | 0.00% | ❌ | N/A
toggle-root (obsolete) | 0.00% | ❌ | N/A
toggle-trigger (obsolete) | 0.00% | ❌ | N/A
toggle-trigger (obsolete) | 0.00% | ❌ | N/A
toggle (obsolete) | 0.00% | ❌ | N/A
toggle (obsolete) | 0.00% | ❌ | N/A
position-fallback | 0.00% | ❌ | N/A
anchor-scroll (obsolete) | 0.00% | ❌ | N/A
anchor-scroll (obsolete) | 0.00% | ❌ | N/A
popover-show-delay | 0.00% | ❌ | N/A
popover-show-delay | 0.00% | ❌ | N/A
popover-show-delay | 0.00% | ❌ | N/A
popover-hide-delay | 0.00% | ❌ | N/A
popover-hide-delay | 0.00% | ❌ | N/A
popover-hide-delay | 0.00% | ❌ | N/A
toggle-visibility (obsolete) | 0.00% | ❌ | N/A
toggle-visibility (obsolete) | 0.00% | ❌ | N/A
animation-delay-start | 0.00% | ❌ | N/A
animation-delay-end | 0.00% | ❌ | N/A
anchor-default (obsolete) | 0.00% | ❌ | N/A
anchor-default (obsolete) | 0.00% | ❌ | N/A
scroll-timeline-attachment | 0.00% | ❌ | N/A
view-timeline-attachment | 0.00% | ❌ | N/A
scroll-start-target-block (obsolete) | 0.00% | ❌ | N/A
scroll-start-target-block (obsolete) | 0.00% | ❌ | N/A
scroll-start-target-inline (obsolete) | 0.00% | ❌ | N/A
scroll-start-target-inline (obsolete) | 0.00% | ❌ | N/A
scroll-start-target-x (obsolete) | 0.00% | ❌ | N/A
scroll-start-target-x (obsolete) | 0.00% | ❌ | N/A
scroll-start-target-y (obsolete) | 0.00% | ❌ | N/A
scroll-start-target-y (obsolete) | 0.00% | ❌ | N/A
position-fallback-bounds | 0.00% | ❌ | N/A
caret-animation | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-ui-4/#propdef-caret-animation)
view-transition-capture-mode | 0.00% | ❌ | N/A
interactivity | 0.00% | ❌ | N/A
text-line-through | 0.00% | ❌ | N/A
text-line-through | 0.00% | ❌ | N/A
text-line-through-color | 0.00% | ❌ | N/A
text-line-through-color | 0.00% | ❌ | N/A
text-line-through-mode | 0.00% | ❌ | N/A
text-line-through-mode | 0.00% | ❌ | N/A
text-line-through-style | 0.00% | ❌ | N/A
text-line-through-style | 0.00% | ❌ | N/A
text-line-through-width | 0.00% | ❌ | N/A
text-line-through-width | 0.00% | ❌ | N/A
text-overline | 0.00% | ❌ | N/A
text-overline | 0.00% | ❌ | N/A
text-overline-color | 0.00% | ❌ | N/A
text-overline-color | 0.00% | ❌ | N/A
text-overline-mode | 0.00% | ❌ | N/A
text-overline-mode | 0.00% | ❌ | N/A
text-overline-style | 0.00% | ❌ | N/A
text-overline-style | 0.00% | ❌ | N/A
text-overline-width | 0.00% | ❌ | N/A
text-overline-width | 0.00% | ❌ | N/A
text-underline | 0.00% | ❌ | N/A
text-underline | 0.00% | ❌ | N/A
text-underline-color (obsolete) | 0.00% | ❌ | N/A
text-underline-color (obsolete) | 0.00% | ❌ | N/A
text-underline-mode (obsolete) | 0.00% | ❌ | N/A
text-underline-mode (obsolete) | 0.00% | ❌ | N/A
text-underline-style | 0.00% | ❌ | N/A
text-underline-style | 0.00% | ❌ | N/A
text-underline-width | 0.00% | ❌ | N/A
text-underline-width | 0.00% | ❌ | N/A
shape-inside | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-round-display/#propdef-shape-inside), [WD](https://www.w3.org/TR/2016/WD-css-round-display-1-20161222/#propdef-shape-inside)
shape-inside | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-round-display/#propdef-shape-inside), [WD](https://www.w3.org/TR/2016/WD-css-round-display-1-20161222/#propdef-shape-inside)
shape-padding | 0.00% | ❌ | N/A
shape-padding | 0.00% | ❌ | N/A
enable-background (obsolete) | 0.00% | ❌ | N/A
enable-background (obsolete) | 0.00% | ❌ | N/A
color-profile (obsolete) | 0.00% | ❌ | N/A
color-profile (obsolete) | 0.00% | ❌ | N/A
glyph-orientation-horizontal (obsolete) | 0.00% | ❌ | N/A
glyph-orientation-horizontal (obsolete) | 0.00% | ❌ | N/A
glyph-orientation-vertical | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-writing-modes-3/#propdef-glyph-orientation-vertical), [ED](https://drafts.csswg.org/css-writing-modes-4/#propdef-glyph-orientation-vertical), [CR](https://www.w3.org/TR/2019/CR-css-writing-modes-4-20190730/#propdef-glyph-orientation-vertical), [REC](https://www.w3.org/TR/2019/REC-css-writing-modes-3-20191210/#propdef-glyph-orientation-vertical)
glyph-orientation-vertical | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-writing-modes-3/#propdef-glyph-orientation-vertical), [ED](https://drafts.csswg.org/css-writing-modes-4/#propdef-glyph-orientation-vertical), [CR](https://www.w3.org/TR/2019/CR-css-writing-modes-4-20190730/#propdef-glyph-orientation-vertical), [REC](https://www.w3.org/TR/2019/REC-css-writing-modes-3-20191210/#propdef-glyph-orientation-vertical)
kerning | 0.00% | ❌ | N/A
kerning | 0.00% | ❌ | N/A
image-orientation | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-images-3/#propdef-image-orientation), [CRD](https://www.w3.org/TR/2023/CRD-css-images-3-20231218/#propdef-image-orientation)
image-orientation | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-images-3/#propdef-image-orientation), [CRD](https://www.w3.org/TR/2023/CRD-css-images-3-20231218/#propdef-image-orientation)
image-resolution | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-images-4/#propdef-image-resolution), [WD](https://www.w3.org/TR/2023/WD-css-images-4-20230217/#propdef-image-resolution)
image-resolution | 0.00% | ❌ | [ED](https://drafts.csswg.org/css-images-4/#propdef-image-resolution), [WD](https://www.w3.org/TR/2023/WD-css-images-4-20230217/#propdef-image-resolution)
max-zoom | 0.00% | ❌ | N/A
min-zoom | 0.00% | ❌ | N/A
user-zoom | 0.00% | ❌ | N/A
internal-callback | 0.00% | ❌ | N/A
internal-callback | 0.00% | ❌ | N/A
touch-action-delay | 0.00% | ❌ | N/A
touch-action-delay | 0.00% | ❌ | N/A
scroll-blocks-on (obsolete) | 0.00% | ❌ | N/A
scroll-blocks-on (obsolete) | 0.00% | ❌ | N/A
motion-rotation | 0.00% | ❌ | N/A
motion-rotation | 0.00% | ❌ | N/A
motion-rotation | 0.00% | ❌ | N/A
scroll-snap-points-x | 0.00% | ❌ | N/A
scroll-snap-points-x | 0.00% | ❌ | N/A
scroll-snap-points-y | 0.00% | ❌ | N/A
scroll-snap-points-y | 0.00% | ❌ | N/A
scroll-snap-coordinate (obsolete) | 0.00% | ❌ | N/A
scroll-snap-coordinate (obsolete) | 0.00% | ❌ | N/A
scroll-snap-destination | 0.00% | ❌ | N/A
scroll-snap-destination | 0.00% | ❌ | N/A
apply-at-rule | 0.00% | ❌ | N/A
apply-at-rule | 0.00% | ❌ | N/A
scroll-customization | 0.00% | ❌ | N/A
viewport-fit | 0.00% | ❌ | N/A
overflow-inline | 0.00% | ✅ | [ED](https://drafts.csswg.org/css-overflow-3/#propdef-overflow-inline), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-overflow-inline)
overflow-block | 0.00% | ✅ | [ED](https://drafts.csswg.org/css-overflow-3/#propdef-overflow-block), [WD](https://www.w3.org/TR/2023/WD-css-overflow-3-20230329/#propdef-overflow-block)
content-size | 0.00% | ❌ | N/A
content-size | 0.00% | ❌ | N/A
render-subtree (obsolete) | 0.00% | ❌ | N/A
render-subtree (obsolete) | 0.00% | ❌ | N/A
origin-trial-test-property | 0.00% | ❌ | N/A
subtree-visibility | 0.00% | ❌ | N/A
subtree-visibility | 0.00% | ❌ | N/A
source | 0.00% | ❌ | N/A
start | 0.00% | ❌ | N/A
end | 0.00% | ❌ | N/A
time-range | 0.00% | ❌ | N/A
letter-spacing-override | 0.00% | ❌ | N/A
letter-spacing-override | 0.00% | ❌ | N/A
object-overflow | 0.00% | ❌ | N/A
top-layer | 0.00% | ❌ | N/A
masonry-track-end | 0.00% | ❌ | N/A
