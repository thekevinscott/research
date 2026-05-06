# Kahana — Built by Agents, Tested by Agents, Trusted by Whom?

Source: https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/

---

Built by Agents, Tested by Agents, Trusted by Whom? - CodeX - Stanford Law School























function is\_browser() {
return (
navigator.userAgent.indexOf( "Chrome" ) !== -1 ||
navigator.userAgent.indexOf( "Opera" ) !== -1 ||
navigator.userAgent.indexOf( "Firefox" ) !== -1 ||
navigator.userAgent.indexOf( "MSIE" ) !== -1 ||
navigator.userAgent.indexOf( "Safari" ) !== -1
);
}
function is\_ie\_6\_7\_8() {
// Feature detection - returns true for IE 6-8
return !document.addEventListener;
}
function is\_ie\_9\_or\_10() {
// User agent detection - returns true for IE 9-10
return (
navigator.userAgent.indexOf( "Trident/5.0" ) !== -1 || // IE9
navigator.userAgent.indexOf( "Trident/6.0" ) !== -1 // IE10
);
}
function not\_excluded\_page() {
return (
window.location.href.indexOf( "/unsupported-browser/" ) === -1 &&
document.title.toLowerCase().indexOf( 'page not found' ) === -1
);
}
if ( is\_browser() && ( is\_ie\_6\_7\_8() || is\_ie\_9\_or\_10() ) && not\_excluded\_page() ) {
// Redirect to unsupported browser page
window.location = location.protocol + '//' + location.host + '/unsupported-browser/';
}

WebFontConfig = {
google : { families: ['Noto+Serif:400,700:latin'] },
typekit: { id: 'jer0mpe' }
};
( function( d ) {
var wf = d.createElement( 'script' ), s = d.scripts[0];
wf.src = 'https://law.stanford.edu/wp-content/themes/stanford-law-school/js/webfontloader.js';
s.parentNode.insertBefore( wf, s );
} )( document );














/\*! This file is auto-generated \*/
.wp-block-button\_\_link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file\_\_button{background:#32373c;color:#fff;text-decoration:none}
/\*# sourceURL=/wp-includes/css/classic-themes.min.css \*/

:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);}:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(\*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(\*, div){margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
/\*# sourceURL=global-styles-inline-css \*/




.white-header {
font-weight: 600;
font-size: 30px;
line-height: 1.1;
color: #ffffff;
}
.white-text {
color: #ffffff;
}
.black-header {
font-weight: 600;
font-size: 30px;
line-height: 1.1;
color: #231F20;
}
.black-text {
color: #231F20;
}
.grey-header {
font-weight: 600;
font-size: 30px;
line-height: 1.1;
color: #404040;
}
.grey-text {
color: #404040;
}
.magenta-header {
font-weight: 600;
font-size: 30px;
line-height: 1.1;
color: #C4122F;
}
.magenta-text {
color: #C4122F;
}
.as-layer {
-webkit-font-smoothing: antialiased;
}
@media (min-width: 768px) {
.white-header {
font-size: 77px;
line-height: 1;
}
}
/\* Adjustments for rollfold \*/
.page-id-334417 [data-url-key="slsnav-discover"] {
margin-top: -20px !important;
}
#accordion-slider-4 #sls-as-nav {
top: 50%;
margin-top: -20px;
height: 0;
padding: 0;
}
#accordion-slider-4 .sls-as-current-page-status {
display: none;
}
#accordion-slider-4 .sls-as-controls-text {
display: none;
}
#accordion-slider-4 #sls-as-controls .sls-as-prev {
margin-left: -36px;
}
#accordion-slider-4 #sls-as-controls .sls-as-next {
margin-right: -36px;
}
/\* Move arrows up for slider 5 \*/
#accordion-slider-5 #sls-as-nav {
top: 50%;
margin-top: -20px;
height: 0;
padding: 0;
}
#accordion-slider-5 .sls-as-current-page-status {
display: none;
}
#accordion-slider-5 .as-pagination-buttons {
display: none;
}
#accordion-slider-5 .sls-as-controls-text {
display: none;
}
#accordion-slider-5 #sls-as-controls .sls-as-prev {
margin-left: -36px;
}
#accordion-slider-5 #sls-as-controls .sls-as-next {
margin-right: -36px;
}
/\* Text styling for large stats \*/
.sls-stat {
color: #fff;
font-size: 90px !important;
width: 100%;
padding: 20px;
}
/\* SLS Stats: sizes \*/
.sls-stat.lg {
font-size: 70px !important;
}
.sls-stat.med {
font-size: 40px !important;
}
.sls-stat.sm {
font-size: 30px !important;
}
.sls-stat.tiny {
font-size: 20px !important;
}
/\* SLS Stats: alignment \*/
.sls-stat.center {
text-align: center;
}
.sls-stat.right {
text-align: right;
}
/\* SLS Stats: color \*/
.sls-stat.red {
color: #B30000;
}
.sls-stat.black {
color: #1A1A1A;
}
.sls-stat.gray {
color: #2b2b2b;
}
.sls-stat-width-auto {
width: auto !important;
}
/\*# sourceURL=accordion-slider-plugin-style-inline-css \*/











// wait for ready event
// jQuery( document ).ready(function() {
// Select the node that will be observed for mutations
const targetNode = document.documentElement;
// Options for the observer (which mutations to observe)
const config = { attributes: false, childList: true, subtree: false };
var bold\_timeline\_item\_button\_done = false;
var css\_override\_item\_done = false;
var css\_override\_group\_done = false;
var css\_override\_container\_done = false;
// Callback function to execute when mutations are observed
const callback = function( mutationsList, observer ) {
var i;
//for ( i = 0; i < mutationsList.length; i++ ) {
//if ( mutationsList[ i ].type === 'childList' ) {
if ( typeof jQuery !== 'undefined' && jQuery( '.bold\_timeline\_item\_button' ).length > 0 && ! bold\_timeline\_item\_button\_done ) {
bold\_timeline\_item\_button\_done = true;
jQuery( '.bold\_timeline\_item\_button' ).each( function() {
var css\_override = jQuery( this ).data( 'css-override' );
if ( css\_override != '' ) {
var id = jQuery( this ).attr( 'id' );
css\_override = css\_override.replace( /(\.bold\_timeline\_item\_button)([\.\{\s])/g, '.bold\_timeline\_item\_button#' + id + '$2' );
var head = document.getElementsByTagName( 'head' )[0];
var style = document.createElement( 'style' );
style.appendChild( document.createTextNode( css\_override ) );
head.appendChild( style );
}
});
}
if ( typeof jQuery !== 'undefined' && jQuery( '.bold\_timeline\_item' ).length > 0 && ! css\_override\_item\_done ) {
css\_override\_item\_done = true;
jQuery( '.bold\_timeline\_item' ).each( function() {
var css\_override = jQuery( this ).data( 'css-override' );
if ( css\_override != '' ) {
var id = jQuery( this ).attr( 'id' );
css\_override = css\_override.replace( /(\.bold\_timeline\_item)([\.\{\s])/g, '.bold\_timeline\_item#' + id + '$2' );
var head = document.getElementsByTagName( 'head' )[0];
var style = document.createElement( 'style' );
style.appendChild( document.createTextNode( css\_override ) );
head.appendChild( style );
}
});
}
if ( typeof jQuery !== 'undefined' && jQuery( '.bold\_timeline\_group' ).length > 0 && ! css\_override\_group\_done ) {
css\_override\_group\_done = true;
jQuery( '.bold\_timeline\_group' ).each( function() {
var css\_override = jQuery( this ).data( 'css-override' );
if ( css\_override != '' ) {
var id = jQuery( this ).attr( 'id' );
css\_override = css\_override.replace( /(\.bold\_timeline\_group)([\.\{\s])/g, '.bold\_timeline\_group#' + id + '$2' );
var head = document.getElementsByTagName( 'head' )[0];
var style = document.createElement( 'style' );
style.appendChild( document.createTextNode( css\_override ) );
head.appendChild( style );
}
});
}
if ( typeof jQuery !== 'undefined' && jQuery( '.bold\_timeline\_container' ).length > 0 && ! css\_override\_container\_done ) {
css\_override\_container\_done = true;
jQuery( '.bold\_timeline\_container' ).each( function() {
var css\_override = jQuery( this ).data( 'css-override' );
if ( css\_override != '' ) {
var id = jQuery( this ).attr( 'id' );
css\_override = css\_override.replace( /(\.bold\_timeline\_container)([\.\{\s])/g, '#' + id + '$2' );
var head = document.getElementsByTagName( 'head' )[0];
var style = document.createElement( 'style' );
style.appendChild( document.createTextNode( css\_override ) );
head.appendChild( style );
}
});
}
//}
//}
};
//}); // ready event
// Create an observer instance linked to the callback function
const observer = new MutationObserver( callback );
// Start observing the target node for configured mutations
observer.observe(targetNode, config);
// Later, you can stop observing
document.addEventListener( 'DOMContentLoaded', function() { observer.disconnect(); }, false );


var cffsiteurl = "https://law.stanford.edu/wp-content/plugins";
var cffajaxurl = "https://law.stanford.edu/wp-admin/admin-ajax.php";
var cfflinkhashtags = "false";
 
(function($) {
$(document).on('facetwp-loaded', function() {
$('.facetwp-facet').each(function() {
var facet = $(this);
var facet\_name = facet.attr('data-name');
var facet\_type = facet.attr('data-type');
var facet\_label = FWP.settings.labels[facet\_name];
if (facet\_type === 'dropdown') {
if (facet.closest('.facet-wrap').length < 1 && facet.closest('.facetwp-flyout').length < 1) {
facet.wrap('<div class="facet-wrap"></div>');
facet.before('<label class="facet-label accessibility" for="' + facet\_name + '">' + facet\_label + '</label>');
}
}
});
});
})(jQuery);

.b-promo-cta {
margin-top: 10px;
}
.cc-simple .wp-image-wrap img,
.cc-simple .wp-caption img {
margin-left: auto;
margin-right: auto;
}
.postid-516676 .it-title {
font-size: 20px;
font-weight: 600;
}
.postid-516676 .it-content h3 {
font-size: 24px;
} 






(function( w, d, s, l, i ) {
w[l] = w[l] || [];
w[l].push( {
'gtm.start': new Date().getTime(), event: 'gtm.js'
} );
var f = d.getElementsByTagName( s )[0],
j = d.createElement( s ), dl = l != 'dataLayer' ? '&l=' + l : '';
j.async = true;
j.src =
'//www.googletagmanager.com/gtm.js?id=' + i + dl;
f.parentNode.insertBefore( j, f );
})( window, document, 'script', 'dataLayer', 'GTM-KZGWGC' );


.cls-4 { fill: #d80001; }  logo-footer                    logo-full                    logo-stanford-university     logo           menu-close  menu       
Close IconIcon with an X to denote closing.  .st0{fill:#FFFFFF;}   
Play IconPlay icon in a circular border.

[Skip to main content](#main-content "#main-content") 

Menu

[SLS](https://law.stanford.edu "Go to the Stanford Law School homepage.")
|[SLS Blogs](https://law.stanford.edu/blog/ "https://law.stanford.edu/blog/")

[SLS Blogs**/**](https://law.stanford.edu/blog/ "https://law.stanford.edu/blog/")[CodeX](https://law.stanford.edu/blog/?tax_and_terms=3520 "https://law.stanford.edu/blog/?tax_and_terms=3520")

Search






Built by Agents, Tested by Agents, Trusted by Whom?
===================================================

* February 8, 2026
* By
  + Eran Kahana

* [Subscribe](/blog-subscription/ "/blog-subscription/")
* [Share on Twitter](https://twitter.com/share?url=https%3A%2F%2Flaw.stanford.edu%2F2026%2F02%2F08%2Fbuilt-by-agents-tested-by-agents-trusted-by-whom%2F&via=StanfordLaw&text=I'm reading: Built by Agents, Tested by Agents, Trusted by Whom? at  "Share on Twitter")
* [Share on Facebook](https://www.facebook.com/sharer/sharer.php?s=100&p[title]=Built+by+Agents%2C+Tested+by+Agents%2C+Trusted+by+Whom%3F&p[url]=https%3A%2F%2Flaw.stanford.edu%2F2026%2F02%2F08%2Fbuilt-by-agents-tested-by-agents-trusted-by-whom%2F&p[images][0]=&p[summary]=On+February+6%2C+2026%2C+StrongDM%E2%80%99s+AI+team+published+a+manifesto.+Three+engineers+described+a+%E2%80%9CSoftware+Factory%E2%80%9D+where+coding+agents+write%2C+test%2C+and+ship+production+software.+No+human+writes+code.+No+human+reviews+code.+The+humans+design+specifications%2C+curate+test+scenarios%2C+and+watch+the+scores.+The+agents+do+everything+else.+This+is+not+a+research+prototype.+StrongDM+builds+access+management+and+security+software.+Pause+on+that.+A+team+building+security+infrastructure+has+decided+that+human+code+review+is+an+obstacle%2C+not+a+safeguard.+They+are+not+alone.+Dan+Shapiro%E2%80%99s+five-level+taxonomy+of+AI-assisted+programming%2C+published+weeks+earlier%2C+places+this+approach+at... "Share on Facebook")

On February 6, 2026, StrongDM’s AI team published a manifesto. Three engineers described a “Software Factory” where coding agents write, test, and ship production software. No human writes code. No human reviews code. The humans design specifications, curate test scenarios, and watch the scores. The agents do everything else.

This is not a research prototype. [StrongDM](https://www.strongdm.com/ "https://www.strongdm.com/") builds access management and security software. Pause on that. A team building *security infrastructure* has decided that human code review is an obstacle, not a safeguard. They are not alone. Dan Shapiro’s [five-level taxonomy of AI-assisted programming](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/ "https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/"), published weeks earlier, places this approach at “Level 5: The Dark Factory.” The term borrows from manufacturing, where robots work in unlit facilities because robots do not need to see.

I think this development is more consequential than it appears. It is not merely a story about productivity. It inverts how we assign responsibility for software behavior. Existing regulatory frameworks are not prepared for it.

**The Inversion**

StrongDM’s charter contains two rules: “Code must not be written by humans” and “Code must not be reviewed by humans.” Their CTO, Justin McCarthy, offers a benchmark: “If you haven’t spent at least $1,000 on tokens today per human engineer, your software factory has room for improvement.”

Why does this work at all? Consider the trajectory. In 2024, models like Claude 3.5 Sonnet and later updates substantially improved at coding tasks, especially when used in agentic workflows over long contexts. By late 2025, newer systems from Anthropic, OpenAI, and others made it routine for many engineers to rely on AI to draft and refactor large portions of production code, with human effort shifting toward architecture, safety, and integration review. By November 2025, newer models from Anthropic and OpenAI made AI-written code reliable enough that the question shifted from “can agents write code?” to “why are humans still writing code?”

This is a textbook example of what Ray Kurzweil calls the Law of Accelerating Returns (the observation that technological progress follows exponential curves, but humans consistently misjudge the pace because we instinctively extrapolate in linear fashion). The exponential curve here is not raw compute. It is model reliability on complex, multi-step tasks. Each generation of model compounds the gains of the last. The shift from human verification to machine-driven validation happened faster than almost anyone predicted, and it will keep accelerating.

But speed raises an alignment question that Stuart Russell has spent decades studying (his work on AI alignment focuses on the gap between what we tell machines to optimize and what we actually want). What are these agents trying to do? The answer is: pass the tests. Not “build good software.” Not “serve the user.” Pass the tests. That’s it. StrongDM learned this the hard way. Their agents [wrote return true](https://factory.strongdm.ai/ "https://factory.strongdm.ai/"), which passes any test beautifully and does nothing useful.

**How Do You Know It Works?**

Instead of checking whether code passes or fails a fixed set of tests, StrongDM wrote detailed descriptions of how a real customer would actually use the software, step by step. They kept these descriptions hidden from the agents, so the agents could not simply memorize the answers. Then they asked a different question than traditional testing asks. Instead of “does it pass?”, they asked “if a real person used this software in all the ways a real person might, how often would it actually do what they needed?”

The [AI Life Cycle Core Principles](https://law.stanford.edu/2023/03/17/ai-life-cycle-core-principles/ "https://law.stanford.edu/2023/03/17/ai-life-cycle-core-principles/") (AILCCP) framework’s Metrics principle warns against exactly this kind of substitution unless done carefully. (Note: AILCCP principles appear in initial uppercase.) The economist Charles Goodhart observed in 1975 that when a measure becomes a target, it ceases to be a good measure. Tell an agent to maximize a test score and it will maximize the test score, whether or not the underlying software actually works. StrongDM’s satisfaction metric is clever, but it uses AI-as-judge. This creates a circularity: the same class of technology that writes the code also decides whether the code works. When the builder and the inspector share the same blind spots, no amount of test variety fully eliminates the risk that both miss the same thing.

The Accuracy principle sharpens this. It requires that AI system performance match what developers and vendors claim, and that the system employ ongoing testing and self-correction. StrongDM does test continuously. But the tests are run by systems with the same limitations as the systems being tested. When a human writes a test, the human brings different assumptions, different mistakes, and different oversights than the person who wrote the code. That mismatch is what makes testing useful. When the same AI model writes the code and evaluates it, that mismatch shrinks.

This is Russell’s alignment problem. The agents are not trying to satisfy users. They are trying to score well on a test that is supposed to represent user satisfaction. Those are different things. A clever enough agent will find ways to ace the test without actually doing what users need. The “return true” episode was a crude version. Subtler versions will be harder to catch.

**The Digital Twin Universe and the Economics of Impossible Things**

The most creative element of StrongDM’s approach is what they call the Digital Twin Universe. They built working replicas of Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets, mimicking their interfaces, edge cases, and behaviors. Against these replicas, they run thousands of test scenarios per hour. No rate limits. No API costs. No risk of breaking real services.

McCarthy frames this as an economic inversion, and the evidence supports him. Building a faithful replica of a major SaaS product was always technically possible. It was never worth the cost. Engineers did not even propose it because they already knew the answer. Then the cost of writing software collapsed. What was unthinkable six months ago is now routine.

This is Kurzweil’s exponential logic again, applied to economics rather than capability. When a technology crosses a cost threshold, investments that were irrational yesterday become obvious today, and the unlocked capabilities cascade. The Digital Twin Universe is not just a testing technique. It is proof that the economics of software have changed in kind, not merely in degree. If you can clone Okta’s API in hours rather than months, the limit on software quality is no longer cost. It is imagination.

But the AILCCP framework’s Accountability principle asks a harder question. When software is “grown” rather than written, when replicas stand in for real services, and when quality is measured by probability rather than certainty, who is responsible for what comes out? The principle requires (among other things) that output be “traceable to an appropriate responsible party” and that there be “zero gap between AI system behavior and deployer’s liability.”

StrongDM’s architecture makes tracing difficult by design. No human reviewed the code that produced a given output. No human wrote the test that validated it. No human built the replica against which it was tested. The humans designed the system that designed the system. Existing legal frameworks assume someone, somewhere, looked at the work. Here, nobody did.

**What Happens to the Engineers?**

StrongDM’s team is three engineers who started in July 2025. By October, when [Simon Willison visited](https://simonwillison.net/2026/Feb/7/software-factory/ "https://simonwillison.net/2026/Feb/7/software-factory/"), they already had working demos of the system that manages their coding agents, their Digital Twin Universe, and their satisfaction testing framework. Three people, three months.

That speed raises a question the AILCCP’s Workforce Compatible principle is designed to surface: does this technology augment human expertise, or does it replace it? StrongDM’s model does not augment software engineering as traditionally understood. It replaces it with something else. The humans in a Software Factory write specifications, design scenarios, and architect systems. They do not program. The skill of reading and writing code, the bedrock of software engineering for seventy years, becomes unnecessary. This is Shapiro’s Level 5, the “Dark Factory,” where the human role shifts entirely from building software to designing and monitoring the systems that build software. The lights are off because nobody needs to see.

The same principle asks a follow-on question: as the old skills fade, does meaningful oversight survive? StrongDM says oversight moves from reviewing code to designing scenarios and monitoring satisfaction. That may prove sufficient. It is also the kind of arrangement where confidence builds gradually, scrutiny fades, and the skills needed to catch a serious failure quietly disappear.

**Regulatory Implications**

So what happens when something goes wrong? Regulation in software has always been reactive. It responds to harm after the fact. The AILCCP framework cannot change that, but it can identify where the gaps are before they produce failures. Three stand out: nobody knows who is liable, nobody knows what to disclose, and the contracts have not caught up.

Accountability in software has historically (and to this day) worked through product liability, professional licensing, and contractual warranties. None of these contemplate software that no human has reviewed. The FTC’s enforcement actions have focused on deceptive marketing and consumer protection. But a Software Factory producing security infrastructure raises different questions entirely. If an access management system fails because an agent-written module contained a subtle error that no human ever saw, who is liable? The three engineers who designed the architecture? The AI provider whose model generated the code? The company that sold the product?

The liability question is hard enough. The disclosure question may be worse. When a customer asks “how was this software built?” the truthful answer is: “Coding agents wrote it. Other agents tested it against replicas of your services. Satisfaction scores exceeded our threshold.” Most procurement officers, auditors, and regulators have no way to evaluate that answer. But the problem runs deeper than unfamiliarity. Even if they understood, they would have no framework for deciding whether the answer is acceptable. No industry standard defines what a sufficient satisfaction score looks like. No audit methodology covers agent-built software tested against replicas. No procurement checklist asks whether the vendor’s coding agents share blind spots with the vendor’s testing agents. The disclosure is technically accurate and practically useless, not because the listener is unsophisticated, but because the tools for making sense of it do not exist yet.

And here is the quiet (or loud) absurdity that deserves attention. Open the terms of service for any AI-built product shipping today. Read the galactic warranty disclaimers, the limitation-of-liability clauses, the “AS IS” language. You will find them virtually identical to the terms that have accompanied software for decades. The same boilerplate that disclaimed liability when dozens of engineers wrote and reviewed every line now disclaims liability when no human has looked at the code at all. The contractual wrapper has not changed while the thing inside the wrapper has. A limitation-of-liability clause drafted for software built by humans, tested by humans, and reviewed by humans is now quietly absorbing the risk of software that was none of those things. Nobody updated the contract because the contract was never designed to describe how the software was made. It was designed to limit–or more accurately–extinguish what happens when the software breaks. And so the same language that once disclaimed imperfection in a human process now disclaims the absence of a human process entirely.

That gap between what the product is and what the contract says creates a credibility problem the AILCCP’s Trustworthy principle identifies directly: blanket disclaimers that contradict a vendor’s own trust claims destroy the trust they are trying to build. Try telling an enterprise customer that your software was never reviewed by a human. Then hand them the same limitation-of-liability clause their vendor used in 1996.

But perhaps this is transitional. The Software Factory represents such a thorough departure from conventional development that it might eventually produce an entirely new contractual form. A vendor confident enough to eliminate human code review might also be confident enough to offer terms that reflect what the product actually is: a warranty tied not to human inspection but to satisfaction scores, scenario coverage, or Digital Twin fidelity, with disclosures covering the agent architecture, the testing methodology, and the threshold at which the vendor considers the software fit for use. Nobody has done this yet, and the reasons are structural. Insurance underwriters price risk based on categories they understand, and “software produced without human review, tested by AI against simulated services” does not appear in any underwriting model. Investors would read novel warranty terms as voluntary assumption of liability. The legacy boilerplate persists because it limits exposure, satisfies insurers, and avoids alarming the board, not because it accurately describes the product.

The liability gap, the disclosure gap, and the contractual gap all point to the same underlying problem. Stuart Russell’s AI alignment asks a deceptively simple question: when we build systems that optimize for the objectives we give them, have we preserved the ability to step in and correct course when those objectives turn out to be wrong? For the Software Factory, the answer is not yet and probably never. No regulatory framework addresses this mode of production at all. And the exponential adoption curve means the window for getting ahead of it is narrow. If StrongDM’s approach spreads at the rate current trends suggest, Software Factories could be producing a significant share of commercial software within two years.

The Software Factory’s greatest risk is not that agent-written code will be worse than human-written code. It may very well be better. The risk is that when it fails, nobody will know why. Nobody will know how to fix it. And the institutional knowledge required to understand the failure will have atrophied, because the humans stopped reading code years ago.

**Category:**

* Uncategorized

**Tags:**

* [AI governance](https://law.stanford.edu/blog/?tax_and_terms=9779&page=1 "https://law.stanford.edu/blog/?tax_and_terms=9779&page=1"),
* [AI risk](https://law.stanford.edu/blog/?tax_and_terms=9871&page=1 "https://law.stanford.edu/blog/?tax_and_terms=9871&page=1"),
* [artificial intelligence](https://law.stanford.edu/blog/?tax_and_terms=4816&page=1 "https://law.stanford.edu/blog/?tax_and_terms=4816&page=1"),
* [Eran Kahana](https://law.stanford.edu/blog/?tax_and_terms=4835&page=1 "https://law.stanford.edu/blog/?tax_and_terms=4835&page=1"),
* [StrongDM](https://law.stanford.edu/blog/?tax_and_terms=9870&page=1 "https://law.stanford.edu/blog/?tax_and_terms=9870&page=1")

* [Subscribe](/blog-subscription/ "/blog-subscription/")
* [Share on Twitter](https://twitter.com/share?url=https%3A%2F%2Flaw.stanford.edu%2F2026%2F02%2F08%2Fbuilt-by-agents-tested-by-agents-trusted-by-whom%2F&via=StanfordLaw&text=I'm reading: Built by Agents, Tested by Agents, Trusted by Whom? at  "Share on Twitter")
* [Share on Facebook](https://www.facebook.com/sharer/sharer.php?s=100&p[title]=Built+by+Agents%2C+Tested+by+Agents%2C+Trusted+by+Whom%3F&p[url]=https%3A%2F%2Flaw.stanford.edu%2F2026%2F02%2F08%2Fbuilt-by-agents-tested-by-agents-trusted-by-whom%2F&p[images][0]=&p[summary]=On+February+6%2C+2026%2C+StrongDM%E2%80%99s+AI+team+published+a+manifesto.+Three+engineers+described+a+%E2%80%9CSoftware+Factory%E2%80%9D+where+coding+agents+write%2C+test%2C+and+ship+production+software.+No+human+writes+code.+No+human+reviews+code.+The+humans+design+specifications%2C+curate+test+scenarios%2C+and+watch+the+scores.+The+agents+do+everything+else.+This+is+not+a+research+prototype.+StrongDM+builds+access+management+and+security+software.+Pause+on+that.+A+team+building+security+infrastructure+has+decided+that+human+code+review+is+an+obstacle%2C+not+a+safeguard.+They+are+not+alone.+Dan+Shapiro%E2%80%99s+five-level+taxonomy+of+AI-assisted+programming%2C+published+weeks+earlier%2C+places+this+approach+at... "Share on Facebook")


Post Pagination

* [Previous Article
  From Logging to Transparency: Locating AI Agent Controls in the AI Life Cycle Core Principles Framework](https://law.stanford.edu/2026/01/31/from-logging-to-hitl-locating-agent-controls-in-the-ai-life-cycle-core-principles-framework/ "https://law.stanford.edu/2026/01/31/from-logging-to-hitl-locating-agent-controls-in-the-ai-life-cycle-core-principles-framework/")
* [Next Article
  Context Stewardship: What Source-by-Source Authorization Misses](https://law.stanford.edu/2026/02/11/context-stewardship-what-source-by-source-authorization-misses/ "https://law.stanford.edu/2026/02/11/context-stewardship-what-source-by-source-authorization-misses/")



Crown Quadrangle  
559 Nathan Abbott Way  
Stanford,
CA
94305-8610

* **Phone:** 650.723.2465
* **Fax:** 650.725.0253

* [Follow Us on X](https://x.com/stanfordlaw "Follow us on X")
* [Follow Us on Facebook](https://www.facebook.com/StanfordLawSchool "Follow us on Facebook")
* [Follow Us on YouTube](https://www.youtube.com/user/stanfordlawschool "Follow us on YouTube")
* [Follow Us on Instagram](https://instagram.com/stanfordlawschool/ "Follow us on Instagram")
* [Follow Us on LinkedIn](https://www.linkedin.com/company/stanford-law-school "Follow us on LinkedIn")
* [Subscribe to our RSS feeds](https://law.stanford.edu/rss-feeds/ "Subscribe to our RSS feeds")


Secondary Navigation

I am ...

1. [Future Student](https://law.stanford.edu/i-am-a-future-student/ "https://law.stanford.edu/i-am-a-future-student/")
2. [Current Student](https://law.stanford.edu/i-am-a-current-student/ "https://law.stanford.edu/i-am-a-current-student/")
3. [I am a Staff Member](https://law.stanford.edu/i-am-a-staff-member/ "https://law.stanford.edu/i-am-a-staff-member/")
4. [I am a Faculty Member](https://law.stanford.edu/i-am-a-faculty-member/ "https://law.stanford.edu/i-am-a-faculty-member/")
5. [Alum](https://law.stanford.edu/i-am-an-alum/ "https://law.stanford.edu/i-am-an-alum/")
6. [Employer](https://law.stanford.edu/i-am-an-employer/ "https://law.stanford.edu/i-am-an-employer/")
7. [Journalist](https://law.stanford.edu/i-am-a-journalist/ "https://law.stanford.edu/i-am-a-journalist/")

About

1. [About SLS](https://law.stanford.edu/about/ "https://law.stanford.edu/about/")
2. [ABA-Required Disclosures](https://law.stanford.edu/aba-required-disclosures/ "https://law.stanford.edu/aba-required-disclosures/")
3. [Visiting Campus](https://law.stanford.edu/visiting-campus/ "https://law.stanford.edu/visiting-campus/")
4. [Web Accessibility](https://www.stanford.edu/site/accessibility "https://www.stanford.edu/site/accessibility")
5. [Website Feedback](https://law.stanford.edu/website-feedback/ "https://law.stanford.edu/website-feedback/")
6. [Giving at SLS](https://law.stanford.edu/giving/ "https://law.stanford.edu/giving/")

Education

1. [Degrees](https://law.stanford.edu/education/degrees/ "https://law.stanford.edu/education/degrees/")
2. [Courses](https://law.stanford.edu/education/courses/ "https://law.stanford.edu/education/courses/")
3. [JD Graduation Information](https://law.stanford.edu/education/jd-graduation-information/ "https://law.stanford.edu/education/jd-graduation-information/")
4. [Executive Education](https://law.stanford.edu/executive-education/ "https://law.stanford.edu/executive-education/")

Research

1. [Faculty Research](https://law.stanford.edu/research/faculty-research/ "https://law.stanford.edu/research/faculty-research/")
2. [Robert Crown Law Library](https://law.stanford.edu/robert-crown-law-library/ "https://law.stanford.edu/robert-crown-law-library/")
3. [Publications](/publications/ "/publications/")
4. [Student Journals](/organizations/?page=1&tax_and_terms=311 "/organizations/?page=1&tax_and_terms=311")

Community

1. [Student Life](https://law.stanford.edu/community/student-life/ "https://law.stanford.edu/community/student-life/")
2. [Events](/events "/events")
3. [Faculty Directory](/directory/?tax_and_terms=1067&page=1 "/directory/?tax_and_terms=1067&page=1")
4. [Organizations](/organizations/ "/organizations/")

Careers

1. [Legal Careers](https://law.stanford.edu/careers/career-possibilities/ "https://law.stanford.edu/careers/career-possibilities/")
2. [Jobs at SLS](https://law.stanford.edu/office-of-human-resources/job-announcements/ "https://law.stanford.edu/office-of-human-resources/job-announcements/")

News & Media

1. [News Center](https://law.stanford.edu/media/ "https://law.stanford.edu/media/")
2. [Media Coverage](/press "/press")
3. [SLS Blogs](/blog/ "/blog/")
4. [Stanford Lawyer Magazine](https://law.stanford.edu/stanford-lawyer-magazine/ "https://law.stanford.edu/stanford-lawyer-magazine/")
5. [Video Center](https://law.stanford.edu/media/video-center/ "https://law.stanford.edu/media/video-center/")
6. [Social Media Hub](https://law.stanford.edu/social-media/ "https://law.stanford.edu/social-media/")
7. [SLS Newsletters](https://law.stanford.edu/media/sls-newsletters/ "https://law.stanford.edu/media/sls-newsletters/")

Stanford University Navigation

1. [Stanford Home](https://www.stanford.edu "https://www.stanford.edu")
2. [Maps & Directions](https://visit.stanford.edu/plan/ "https://visit.stanford.edu/plan/")
3. [Search Stanford](https://www.stanford.edu/search/ "https://www.stanford.edu/search/")
4. [Emergency Info](https://emergency.stanford.edu "https://emergency.stanford.edu")


Legal Navigation

1. [Terms of Use](https://www.stanford.edu/site/terms/ "https://www.stanford.edu/site/terms/")
2. [Privacy](https://www.stanford.edu/site/privacy/ "https://www.stanford.edu/site/privacy/")
3. [Copyright](https://uit.stanford.edu/security/copyright-infringement "https://uit.stanford.edu/security/copyright-infringement")
4. [Trademarks](https://adminguide.stanford.edu/chapter-1/subchapter-5/policy-1-5-4 "https://adminguide.stanford.edu/chapter-1/subchapter-5/policy-1-5-4")
5. [Non-Discrimination](https://exploredegrees.stanford.edu/nonacademicregulations/nondiscrimination/ "https://exploredegrees.stanford.edu/nonacademicregulations/nondiscrimination/")
6. [Accessibility](https://www.stanford.edu/site/accessibility "https://www.stanford.edu/site/accessibility")

©
Stanford University,
Stanford,
California
94305.

Back to the Top


© Stanford University, Stanford, California, 94305-8610 | https://law.stanford.edu/2026/02/08/built-by-agents-tested-by-agents-trusted-by-whom/ 

{"prefetch":[{"source":"document","where":{"and":[{"href\_matches":"/\*"},{"not":{"href\_matches":["/wp-\*.php","/wp-admin/\*","/wp-content/uploads/\*","/wp-content/\*","/wp-content/plugins/\*","/wp-content/themes/stanford-law-school/\*","/\*\\?(.+)"]}},{"not":{"selector\_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector\_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}

( function ( body ) {
'use strict';
body.className = body.className.replace( /\btribe-no-js\b/, 'tribe-js' );
} )( document.body );





var sbiajaxurl = "https://law.stanford.edu/wp-admin/admin-ajax.php";
 /\* <![CDATA[ \*/var tribe\_l10n\_datatables = {"aria":{"sort\_ascending":": activate to sort column ascending","sort\_descending":": activate to sort column descending"},"length\_menu":"Show \_MENU\_ entries","empty\_table":"No data available in table","info":"Showing \_START\_ to \_END\_ of \_TOTAL\_ entries","info\_empty":"Showing 0 to 0 of 0 entries","info\_filtered":"(filtered from \_MAX\_ total entries)","zero\_records":"No matching records found","search":"Search:","all\_selected\_text":"All items on this page were selected. ","select\_all\_link":"Select all pages","clear\_selection":"Clear Selection.","pagination":{"all":"All","next":"Next","previous":"Previous"},"select":{"rows":{"0":"","\_":": Selected %d rows","1":": Selected 1 row"}},"datepicker":{"dayNames":["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"dayNamesShort":["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],"dayNamesMin":["S","M","T","W","T","F","S"],"monthNames":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesShort":["January","February","March","April","May","June","July","August","September","October","November","December"],"monthNamesMin":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"nextText":"Next","prevText":"Prev","currentText":"Today","closeText":"Done","today":"Today","clear":"Clear"}};/\* ]]> \*/ 

/\* <![CDATA[ \*/
var cffOptions = {"placeholder":"https://law.stanford.edu/wp-content/plugins/custom-facebook-feed-pro/assets/img/placeholder.png","resized\_url":"http://law.stanford.edu/wp-content/uploads/sb-facebook-feed-images/","nonce":"61a7747b45"};
//# sourceURL=cffscripts-js-extra
/\* ]]> \*/



/\* <![CDATA[ \*/
var modern\_tribe\_i18n = {"nav":{"button\_hide":"Hide","explore\_cell\_1":"I am a Future student","explore\_cell\_2":"I am a Current Student","explore\_cell\_3":"I am a Faculty/Staff Member","explore\_cell\_4":"I am an Alumna/Alumnus","explore\_cell\_5":"I am an Employer","explore\_cell\_6":"I am a Journalist","label\_explore":"Explore","link\_home":"Go to the Stanford Law School homepage.","placeholder\_search":"Search","logged\_out\_label":"SLS Login","logged\_in\_label":"SLS Logout","admin\_link\_label":"Dashboard","title\_close":"Close main website navigation menu."},"jump\_nav":{"btn\_jumpto":"Jump to","btn\_top":"Top","btn\_prev":"Prev","btn\_next":"Next","btn\_facebook":"Share on Facebook.","btn\_twitter":"Share on Twitter.","btn\_google\_plus":"Share on Google Plus.","twitter\_msg":"I'm reading: %s at "},"search":{"placeholder":"Search SLS"},"tooltips":{"menu\_prompt\_copy":"Click here to toggle the section navigation."},"donation":{"header":"Please support the China Guiding Cases Project.","body":"Only with your support can we continue to offer products of the highest quality available for free download. Make a contribution today to support the development of Chinese law tomorrow.","yes\_btn":"Yes, the CGCP's great work deserves support","no\_btn":"No, I want to observe more before I offer assistance"},"download":{"header":"The CGCP provides top-notch products at no cost. To help us understand our readers' needs, we ask for the following information, which will be kept confidential.","name\_label":"Name","name\_placeholder":"Enter Name","email\_label":"Email","email\_placeholder":"Enter Email Address","age\_label":"Age","age\_placeholder":"Choose Age Group","occupation\_label":"Occupation","occupation\_placeholder":"Your Occupation","submit\_btn":"Submit","form\_footer":"The information collected will be added to the CGCP user list upon submission.","download\_btn":"Download Now","form\_confirmation\_header":"Thanks for supporting the China Guiding Cases Project. This product is now available for download.","form\_confirmation\_body":"Your subscription has been confirmed. You have been added to our list and will hear from us soon.","form\_error\_header":"Oops!"},"loop":{"surveys":{"label\_issue\_number":"Issue No.:","label\_publication\_date":"Date of Publication:","label\_authors":"Author(s):","issue\_title":"Survey Issue No. %s"},"analytics":{"label\_publication\_date":"Date of Publication:"},"commentaries":{"label\_publication\_date":"Date of Publication:","label\_author\_and\_title":"Author(s):","alternative\_title":"No. %s: %s"},"guiding\_cases":{"label\_released\_date":"Date of Release:","related\_cases\_text":"Subsequent Cases: %s"},"judgments":{"label\_adjudication\_date":"Date of Adjudication:"},"br\_cases":{"label\_released\_date":"Date of Release:"},"br\_texts":{"label\_signing\_date":"Signing Date:","label\_effective\_date":"Effective Date:"},"clc\_spotlight":{"label\_publication\_date":"Date of Publication:"},"selects":{"type\_prompt":"Type to Filter"},"course":{"label\_limitations":"Enrollment Limitations:","label\_units":"Units","label\_all":"All","label\_exams":"Exam:","glaw\_term\_name\_1ljdopen\_human":"1L Winter Elective","glaw\_term\_name\_1llaw\_human":"1L Mandatory","glaw\_term\_name\_globalquar\_human":"Global Quarter","glaw\_term\_name\_shortcours\_human":"Short Course","glaw\_term\_name\_newcourse\_human":"New Course"},"exams":{"time\_separator":"to"},"news":{"title":"SLS News","title\_type":"News & Media","label\_professors":"Related Person(s):","label\_organizations":"Related Organization(s):"},"podcast":{"title":"SLS Podcasts"},"publications":{"attachment\_label":"Download","abstract\_label":"Abstract","newtab\_label":"Opens in a new tab"},"blog":{"title":"SLS Blogs","label\_date":"Date:","author\_label":"By","subscribe\_link":"Subscribe"},"article":{"issue\_label":"Issue"},"directory":{"room\_label":"Room:"},"myc":{"home\_label":"Hometown:","res\_label":"SU Residence:","ed\_label":"Education:","show\_more":"[ + MORE ]","show\_less":"[ - LESS ]","ed\_heading":"Education","work\_heading":"Recent Work Experience","facts\_heading":"Other Interesting Facts","hobbies\_label":"Hobbies:","facts\_label":"Interesting Facts:","family\_label":"Family/SO:"},"pagination":{"headline":"Loop Pagination","next":"Next","prev":"Previous","last":"Last","first":"First"},"no\_results":{"message":"There are currently no results based on your filtering criteria. Please remove some of the existing filters and try again.","selectize":"No results"},"result\_label":{"filtered\_singular":"%s Result For:","filtered\_plural":"%s Results For:","unfiltered":"%s Results"},"reset\_all":"Clear all filters"}};
var modern\_tribe\_config = {"images\_url":"https://law.stanford.edu/wp-content/themes/stanford-law-school/img/","home\_url":"https://law.stanford.edu","template\_url":"https://law.stanford.edu/wp-content/themes/stanford-law-school/","post\_type":"post","date\_format":"F j, Y","archive\_post\_type":"posts","course\_type":"","json\_root":"https://law.stanford.edu/wp-json/wp/v2","json\_nonce":"f1218cf42a","posts\_per\_page":"25","is\_user\_logged\_in":"","admin\_url":"https://law.stanford.edu/wp-admin/","is\_main\_site":"1","is\_cgc\_site":"","is\_myc\_page":"","login\_url":"https://law.stanford.edu/wp-login.php?redirect\_to=https%3A%2F%2Flaw.stanford.edu%2F2026%2F02%2F08%2Fbuilt-by-agents-tested-by-agents-trusted-by-whom%2F&group=sls","logout\_url":"https://law.stanford.edu/wp-login.php?action=logout&redirect\_to=https%3A%2F%2Flaw.stanford.edu%2F2026%2F02%2F08%2Fbuilt-by-agents-tested-by-agents-trusted-by-whom%2F&\_wpnonce=b9beb3dcb4","share\_data":{"post\_url":"https%3A%2F%2Flaw.stanford.edu%2F2026%2F02%2F08%2Fbuilt-by-agents-tested-by-agents-trusted-by-whom%2F","post\_title":"Built+by+Agents%2C+Tested+by+Agents%2C+Trusted+by+Whom%3F","post\_title\_readable":"Built by Agents, Tested by Agents, Trusted by Whom?","fb\_excerpt":"On+February+6%2C+2026%2C+StrongDM%E2%80%99s+AI+team+published+a+manifesto.+Three+engineers+described+a+%E2%80%9CSoftware+Factory%E2%80%9D+where+coding+agents+write%2C+test%2C+and+ship+production+software.+No+human+writes+code.+No+human+reviews+code.+The+humans+design+specifications%2C+curate+test+scenarios%2C+and+watch+the+scores.+The+agents+do+everything+else.+This+is+not+a+research+prototype.+StrongDM+builds+access+management+and+security+software.+Pause+on+that.+A+team+building+security+infrastructure+has+decided+that+human+code+review+is+an+obstacle%2C+not+a+safeguard.+They+are+not+alone.+Dan+Shapiro%E2%80%99s+five-level+taxonomy+of+AI-assisted+programming%2C+published+weeks+earlier%2C+places+this+approach+at...","image\_src":""},"post\_types":{"section":"sections","exam\_schedule":"exam\_schedule","person":"person","organization":"organization","news":"news","publication":"publication","podcast":"podcast","article":"lawyer-article","evaluation":"evaluation","externship":"externship","analytics":"analytics","commentary":"commentary","guiding\_case":"guiding\_case","subsequent\_case":"subsequent\_case","survey":"survey","judgment":"judgment","br\_case":"br\_case","br\_text":"br\_text","br\_country":"br\_country","clc\_spotlight":"clc\_spotlight","masthead":"masthead","project":"project","sls\_archived\_events":"sls\_archived\_events","faculty\_workshops":"faculty\_workshops"},"jump\_nav\_align":"right","rss\_page\_url":"https://law.stanford.edu/rss-feeds/"};
//# sourceURL=sls-theme-scripts-js-extra
/\* ]]> \*/


/\* <![CDATA[ \*/
var gforms\_recaptcha\_recaptcha\_strings = {"nonce":"0838044521","disconnect":"Disconnecting","change\_connection\_type":"Resetting","spinner":"https://law.stanford.edu/wp-content/plugins/gravityforms/images/spinner.svg","connection\_type":"classic","disable\_badge":"1","change\_connection\_type\_title":"Change Connection Type","change\_connection\_type\_message":"Changing the connection type will delete your current settings. Do you want to proceed?","disconnect\_title":"Disconnect","disconnect\_message":"Disconnecting from reCAPTCHA will delete your current settings. Do you want to proceed?","site\_key":"6LdpGtMqAAAAAHWrk3Qboxi2L0VWXMAmSbI92QnB"};
//# sourceURL=gforms\_recaptcha\_recaptcha-js-extra
/\* ]]> \*/





{"menu\_items":[{"label":"About","id":"menu-item-5222","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5222","url":"https:\/\/law.stanford.edu\/about\/","menu\_id":5222,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-1358","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-1358","url":"https:\/\/law.stanford.edu\/about\/","menu\_id":1358,"has\_children":false},{"label":"Why SLS?","id":"menu-item-441301","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-441301","url":"https:\/\/law.stanford.edu\/about\/why-sls\/","menu\_id":441301,"has\_children":false},{"label":"ABA-Required Disclosures","id":"menu-item-1357","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-1357","url":"https:\/\/law.stanford.edu\/aba-required-disclosures\/","menu\_id":1357,"has\_children":false},{"label":"History","id":"menu-item-1356","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-1356","url":"https:\/\/law.stanford.edu\/about\/history\/","menu\_id":1356,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-51377","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-51377","url":"https:\/\/law.stanford.edu\/about\/history\/","menu\_id":51377,"has\_children":false},{"label":"Special Collections","id":"menu-item-51282","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-51282","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/rcll-special-collections\/","menu\_id":51282,"has\_children":false},{"label":"The Ralston Prize","id":"menu-item-51333","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-51333","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/rcll-special-collections\/the-ralston-prize\/","menu\_id":51333,"has\_children":false}]},{"label":"SLS 125","id":"menu-item-229841","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-229841","url":"https:\/\/law.stanford.edu\/sls-125\/","menu\_id":229841,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-229848","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-229848","url":"https:\/\/law.stanford.edu\/sls-125\/","menu\_id":229848,"has\_children":false},{"label":"SLS Moments","id":"menu-item-245109","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-245109","url":"https:\/\/law.stanford.edu\/sls-125\/sls-moments\/","menu\_id":245109,"has\_children":false},{"label":"SLS Stories Archive","id":"menu-item-236438","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-236438","url":"https:\/\/law.stanford.edu\/sls-125\/sls-stories\/","menu\_id":236438,"has\_children":false},{"label":"SLS Timeline","id":"menu-item-229845","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-229845","url":"https:\/\/law.stanford.edu\/sls-125\/sls-timeline\/","menu\_id":229845,"has\_children":false},{"label":"60+ Moments in the History of Stanford Law School","id":"menu-item-229847","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-229847","url":"https:\/\/law.stanford.edu\/sls-125\/60-moments\/","menu\_id":229847,"has\_children":false},{"label":"Where\u2019s SLS?","id":"menu-item-229846","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-229846","url":"https:\/\/law.stanford.edu\/sls-125\/map-of-sls-locations\/","menu\_id":229846,"has\_children":false}]},{"label":"Visiting Campus","id":"menu-item-1360","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-1360","url":"https:\/\/law.stanford.edu\/visiting-campus\/","menu\_id":1360,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-14133","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-14133","url":"https:\/\/law.stanford.edu\/visiting-campus\/","menu\_id":14133,"has\_children":false},{"label":"Driving Directions","id":"menu-item-14134","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-14134","url":"https:\/\/law.stanford.edu\/visiting-campus\/driving-directions\/","menu\_id":14134,"has\_children":false},{"label":"Traveling by Airplane","id":"menu-item-153776","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-153776","url":"https:\/\/law.stanford.edu\/traveling-by-airplane\/","menu\_id":153776,"has\_children":false},{"label":"Public Transportation","id":"menu-item-14137","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-14137","url":"https:\/\/law.stanford.edu\/visiting-campus\/public-transportation\/","menu\_id":14137,"has\_children":false},{"label":"Maps","id":"menu-item-14135","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-14135","url":"https:\/\/law.stanford.edu\/visiting-campus\/maps\/","menu\_id":14135,"has\_children":false}]},{"label":"Giving to SLS","id":"menu-item-306408","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-306408","url":"https:\/\/law.stanford.edu\/giving\/","menu\_id":306408,"has\_children":false}]},{"label":"Education","id":"menu-item-5231","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5231","url":"https:\/\/law.stanford.edu\/education\/","menu\_id":5231,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-1386","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-1386","url":"https:\/\/law.stanford.edu\/education\/","menu\_id":1386,"has\_children":false},{"label":"Degrees","id":"menu-item-1387","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-1387","url":"https:\/\/law.stanford.edu\/education\/degrees\/","menu\_id":1387,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-5265","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-5265","url":"https:\/\/law.stanford.edu\/education\/degrees\/","menu\_id":5265,"has\_children":false},{"label":"JD Program","id":"menu-item-24547","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-24547","url":"https:\/\/law.stanford.edu\/education\/degrees\/jd-program\/","menu\_id":24547,"has\_children":false},{"label":"Joint Degree and Cooperative Programs","id":"menu-item-24525","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-24525","url":"https:\/\/law.stanford.edu\/education\/degrees\/joint-degrees-within-stanford-university\/","menu\_id":24525,"has\_children":false},{"label":"Advanced Degree Programs","id":"menu-item-24546","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-24546","url":"https:\/\/law.stanford.edu\/education\/degrees\/advanced-degree-programs\/","menu\_id":24546,"has\_children":false}]},{"label":"Courses","id":"menu-item-40421","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-40421","url":"https:\/\/law.stanford.edu\/education\/courses\/","menu\_id":40421,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-40420","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-40420","url":"https:\/\/law.stanford.edu\/education\/courses\/","menu\_id":40420,"has\_children":false},{"label":"Course Catalog","id":"menu-item-40423","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-40423","url":"\/courses\/","menu\_id":40423,"has\_children":false},{"label":"SLS Approved Non-Law Courses","id":"menu-item-292888","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-292888","url":"https:\/\/law.stanford.edu\/nl-course\/","menu\_id":292888,"has\_children":false},{"label":"Academic Calendar","id":"menu-item-57466","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-57466","url":"\/education\/courses\/calendar-deadlines\/#slsnav-academic-calendars","menu\_id":57466,"has\_children":false},{"label":"Deadlines","id":"menu-item-41439","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-41439","url":"https:\/\/law.stanford.edu\/education\/courses\/calendar-deadlines\/","menu\_id":41439,"has\_children":false},{"label":"Registration for Law Students","id":"menu-item-40488","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-40488","url":"https:\/\/law.stanford.edu\/education\/courses\/law-students\/","menu\_id":40488,"has\_children":false},{"label":"Registration for Non-Law Students","id":"menu-item-40487","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-40487","url":"https:\/\/law.stanford.edu\/education\/courses\/non-law-students\/","menu\_id":40487,"has\_children":false},{"label":"Textbook Lists","id":"menu-item-40489","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-40489","url":"https:\/\/law.stanford.edu\/education\/courses\/stanford-law-textbook-lists\/","menu\_id":40489,"has\_children":false},{"label":"Consent of Instructor Forms","id":"menu-item-40491","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-40491","url":"https:\/\/law.stanford.edu\/education\/courses\/consent-of-instructor-forms\/","menu\_id":40491,"has\_children":false},{"label":"Exams and Papers","id":"menu-item-54259","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-54259","url":"https:\/\/law.stanford.edu\/education\/courses\/exams-and-papers\/","menu\_id":54259,"has\_children":false},{"label":"Forms and Petitions","id":"menu-item-54260","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-54260","url":"https:\/\/law.stanford.edu\/education\/courses\/forms-and-petitions\/","menu\_id":54260,"has\_children":false}]},{"label":"JD Graduation Requirements","id":"menu-item-54289","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-54289","url":"https:\/\/law.stanford.edu\/education\/jd-graduation-information\/","menu\_id":54289,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-54290","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-54290","url":"https:\/\/law.stanford.edu\/education\/jd-graduation-information\/","menu\_id":54290,"has\_children":false},{"label":"JD Graduation Unit Limitation","id":"menu-item-54294","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-54294","url":"https:\/\/law.stanford.edu\/education\/jd-graduation-information\/jd-graduation-unit-limitation\/","menu\_id":54294,"has\_children":false},{"label":"Specific Graduation Requirements","id":"menu-item-54293","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-54293","url":"https:\/\/law.stanford.edu\/education\/jd-graduation-information\/courses-approved-by-the-curriculum-committee-to-meet-specific-graduation-requirements\/","menu\_id":54293,"has\_children":false}]},{"label":"Interdisciplinary Learning","id":"menu-item-1395","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-1395","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/interdisciplinary-learning\/","menu\_id":1395,"has\_children":false},{"label":"Mills Legal Clinic","id":"menu-item-564218","classes":" menu-item menu-item-type-post\_type menu-item-object-organization menu-item-564218","url":"https:\/\/law.stanford.edu\/mills-legal-clinic\/","menu\_id":564218,"has\_children":false},{"label":"Only-at-SLS","id":"menu-item-546459","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-546459","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/","menu\_id":546459,"has\_children":false},{"label":"Stanford Law AI Initiative","id":"menu-item-559065","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-559065","url":"https:\/\/law.stanford.edu\/ai-initiative\/","menu\_id":559065,"has\_children":false},{"label":"Law &amp; Policy Lab","id":"menu-item-1391","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-1391","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/","menu\_id":1391,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-77789","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-77789","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/","menu\_id":77789,"has\_children":false},{"label":"Policy Reports and Other Deliverables","id":"menu-item-197235","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-197235","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/policy-reports-and-other-deliverables\/","menu\_id":197235,"has\_children":false},{"label":"Practicums 2025-2026","id":"menu-item-527323","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-527323","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/practicums-2025-2026\/","menu\_id":527323,"has\_children":false},{"label":"Past Practicums","id":"menu-item-313538","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-313538","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/past-practicums\/","menu\_id":313538,"has\_children":false},{"label":"Policy Lab Resources","id":"menu-item-431826","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-431826","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/policy-lab-resources\/","menu\_id":431826,"has\_children":false},{"label":"Master Skills Classes","id":"menu-item-40492","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-40492","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/master-skills-classes\/","menu\_id":40492,"has\_children":false},{"label":"Policy Communications Consultation","id":"menu-item-38260","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-38260","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/communications-consultant\/","menu\_id":38260,"has\_children":false},{"label":"Policy Analysis and Advocacy Skills","id":"menu-item-37856","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-37856","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/communications-resources\/","menu\_id":37856,"has\_children":false},{"label":"Law &#038; Policy Lab Blog","id":"menu-item-166077","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-166077","url":"https:\/\/law.stanford.edu\/blog\/?tax\_and\_terms=3141","menu\_id":166077,"has\_children":false},{"label":"Events","id":"menu-item-202993","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-202993","url":"https:\/\/law.stanford.edu\/education\/only-at-sls\/law-policy-lab\/policy-lab-events\/","menu\_id":202993,"has\_children":false}]},{"label":"International and Global Opportunities","id":"menu-item-269792","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-269792","url":"https:\/\/law.stanford.edu\/education\/international-and-global-opportunities\/","menu\_id":269792,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-269793","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-269793","url":"https:\/\/law.stanford.edu\/education\/international-and-global-opportunities\/","menu\_id":269793,"has\_children":false},{"label":"W. A. Franke Global Law Program","id":"menu-item-40410","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-40410","url":"https:\/\/law.stanford.edu\/education\/international-and-global-opportunities\/global-law-program\/","menu\_id":40410,"has\_children":false},{"label":"International and Global Law","id":"menu-item-269804","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-269804","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/international-and-global-law\/","menu\_id":269804,"has\_children":false},{"label":"Foreign Exchange Program for SLS Students","id":"menu-item-40501","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-40501","url":"https:\/\/law.stanford.edu\/education\/international-and-global-opportunities\/foreign-exchange-program-for-sls-students\/","menu\_id":40501,"has\_children":false},{"label":"Visiting Exchange Students Program Info","id":"menu-item-57903","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-57903","url":"https:\/\/law.stanford.edu\/education\/international-and-global-opportunities\/visiting-exchange-students-program-info\/","menu\_id":57903,"has\_children":false}]},{"label":"Discussion Seminars","id":"menu-item-40411","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-40411","url":"https:\/\/law.stanford.edu\/discussion-seminars\/","menu\_id":40411,"has\_children":false},{"label":"Legal Research and Writing Program","id":"menu-item-438789","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-438789","url":"https:\/\/law.stanford.edu\/education\/legal-research-and-writing-program\/","menu\_id":438789,"has\_children":false},{"label":"Short Courses","id":"menu-item-546589","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-546589","url":"https:\/\/law.stanford.edu\/education\/courses\/short-courses\/","menu\_id":546589,"has\_children":false},{"label":"S-Term","id":"menu-item-430084","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-430084","url":"https:\/\/law.stanford.edu\/education\/s-term\/","menu\_id":430084,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-430088","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-430088","url":"https:\/\/law.stanford.edu\/education\/s-term\/","menu\_id":430088,"has\_children":false},{"label":"Past S-Term Offerings","id":"menu-item-465551","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-465551","url":"https:\/\/law.stanford.edu\/education\/s-term\/past-offerings\/","menu\_id":465551,"has\_children":false}]},{"label":"Executive Education","id":"menu-item-551687","classes":" menu-item menu-item-type-post\_type menu-item-object-organization menu-item-551687","url":"https:\/\/law.stanford.edu\/executive-education\/","menu\_id":551687,"has\_children":false},{"label":"Special Programs","id":"menu-item-391398","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-391398","url":"https:\/\/law.stanford.edu\/education\/special-programs\/","menu\_id":391398,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-391399","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-391399","url":"https:\/\/law.stanford.edu\/education\/special-programs\/","menu\_id":391399,"has\_children":false},{"label":"Envision Intensive Law &#038; Trial","id":"menu-item-54307","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-54307","url":"https:\/\/law.stanford.edu\/education\/special-programs\/envision-collaborates-with-stanford-law-school\/","menu\_id":54307,"has\_children":false},{"label":"Stanford Law Scholars Institute","id":"menu-item-323471","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-323471","url":"https:\/\/law.stanford.edu\/education\/special-programs\/stanford-law-scholars-institute\/","menu\_id":323471,"has\_children":false}]}]},{"label":"Apply","id":"menu-item-5230","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5230","url":"https:\/\/law.stanford.edu\/apply\/","menu\_id":5230,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-1366","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-1366","url":"https:\/\/law.stanford.edu\/apply\/","menu\_id":1366,"has\_children":false},{"label":"How to Apply","id":"menu-item-1365","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-1365","url":"https:\/\/law.stanford.edu\/apply\/how-to-apply\/","menu\_id":1365,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-13978","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-13978","url":"https:\/\/law.stanford.edu\/apply\/how-to-apply\/","menu\_id":13978,"has\_children":false},{"label":"JD Application Process","id":"menu-item-6244","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-6244","url":"https:\/\/law.stanford.edu\/apply\/how-to-apply\/jd-application-process\/","menu\_id":6244,"has\_children":false},{"label":"JD Transfer Application Process","id":"menu-item-6245","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-6245","url":"https:\/\/law.stanford.edu\/apply\/how-to-apply\/transfer-application-process\/","menu\_id":6245,"has\_children":false},{"label":"Visiting Student Program","id":"menu-item-6243","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-6243","url":"https:\/\/law.stanford.edu\/apply\/how-to-apply\/visiting-student-program\/","menu\_id":6243,"has\_children":false},{"label":"Joint Degree Application Process","id":"menu-item-14247","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-14247","url":"https:\/\/law.stanford.edu\/apply\/how-to-apply\/joint-degree-application-process\/","menu\_id":14247,"has\_children":false},{"label":"Advanced Degree Application Process","id":"menu-item-14250","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-14250","url":"https:\/\/law.stanford.edu\/apply\/how-to-apply\/advanced-degree-application-process\/","menu\_id":14250,"has\_children":false}]},{"label":"Tuition &amp; Financial Aid","id":"menu-item-1364","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-1364","url":"https:\/\/law.stanford.edu\/apply\/tuition-financial-aid\/","menu\_id":1364,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-22707","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-22707","url":"https:\/\/law.stanford.edu\/apply\/tuition-financial-aid\/","menu\_id":22707,"has\_children":false},{"label":"Cost of Attendance","id":"menu-item-22708","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-22708","url":"https:\/\/law.stanford.edu\/apply\/tuition-financial-aid\/cost-of-attendance\/","menu\_id":22708,"has\_children":false},{"label":"JD Financial Support","id":"menu-item-22709","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-22709","url":"https:\/\/law.stanford.edu\/apply\/tuition-financial-aid\/jd-financial-support\/","menu\_id":22709,"has\_children":false},{"label":"Joint Degree Financial Support","id":"menu-item-25005","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-25005","url":"https:\/\/law.stanford.edu\/apply\/tuition-financial-aid\/joint-degree-financial-support\/","menu\_id":25005,"has\_children":false},{"label":"Advanced Degree Financial Support","id":"menu-item-23071","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-23071","url":"https:\/\/law.stanford.edu\/apply\/tuition-financial-aid\/advanced-degree-financial-support\/","menu\_id":23071,"has\_children":false},{"label":"Loan Repayment Assistance Program (LRAP)","id":"menu-item-22921","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-22921","url":"https:\/\/law.stanford.edu\/apply\/tuition-financial-aid\/loan-repayment-assistance-program-lrap\/","menu\_id":22921,"has\_children":false}]}]},{"label":"Areas of Interest","id":"menu-item-119575","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-119575","url":"https:\/\/law.stanford.edu\/areas-of-interest\/","menu\_id":119575,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-119574","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-119574","url":"https:\/\/law.stanford.edu\/areas-of-interest\/","menu\_id":119574,"has\_children":false},{"label":"Academia","id":"menu-item-28315","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-28315","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/academia\/","menu\_id":28315,"has\_children":false},{"label":"American Indian &#038; Indigenous Law","id":"menu-item-391381","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-391381","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/american-indian-and-indigenous-law\/","menu\_id":391381,"has\_children":false},{"label":"Artificial Intelligence and Law","id":"menu-item-524752","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-524752","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/artificial-intelligence\/","menu\_id":524752,"has\_children":false},{"label":"Clinical Legal Education","id":"menu-item-61694","classes":" menu-item menu-item-type-post\_type menu-item-object-organization menu-item-61694","url":"https:\/\/law.stanford.edu\/mills-legal-clinic\/","menu\_id":61694,"has\_children":false},{"label":"Constitutional Law","id":"menu-item-391383","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-391383","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/constitutional-law\/","menu\_id":391383,"has\_children":false},{"label":"Criminal Law","id":"menu-item-61691","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-61691","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/criminal-law\/","menu\_id":61691,"has\_children":false},{"label":"Environmental Law and Policy","id":"menu-item-366580","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-366580","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/environmental-law-and-policy\/","menu\_id":366580,"has\_children":false},{"label":"Health Law and Policy","id":"menu-item-28317","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-28317","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/health-law-and-policy\/","menu\_id":28317,"has\_children":false},{"label":"International and Global Law","id":"menu-item-28318","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-28318","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/international-and-global-law\/","menu\_id":28318,"has\_children":false},{"label":"Law and History","id":"menu-item-389189","classes":" menu-item menu-item-type-post\_type menu-item-object-organization menu-item-389189","url":"https:\/\/law.stanford.edu\/stanford-center-for-law-and-history\/","menu\_id":389189,"has\_children":false},{"label":"Law and Public Policy","id":"menu-item-329231","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-329231","url":"https:\/\/law.stanford.edu\/public-policy-and-social-problem-solving\/","menu\_id":329231,"has\_children":false},{"label":"Law, Economics, and Business","id":"menu-item-28325","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-28325","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/law-economics-business\/","menu\_id":28325,"has\_children":false},{"label":"Public Service and Public Interest Law","id":"menu-item-28326","classes":" menu-item menu-item-type-post\_type menu-item-object-organization menu-item-28326","url":"https:\/\/law.stanford.edu\/levin-center\/","menu\_id":28326,"has\_children":false},{"label":"Racial Justice","id":"menu-item-342078","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-342078","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/racial-justice\/","menu\_id":342078,"has\_children":false},{"label":"Tech Law and Policy","id":"menu-item-350355","classes":" menu-item menu-item-type-post\_type menu-item-object-area\_of\_interest menu-item-350355","url":"https:\/\/law.stanford.edu\/areas\_of\_interest\/tech-law-and-policy\/","menu\_id":350355,"has\_children":false}]},{"label":"Faculty &#038; Research","id":"menu-item-5234","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5234","url":"https:\/\/law.stanford.edu\/research\/","menu\_id":5234,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-3803","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-3803","url":"https:\/\/law.stanford.edu\/research\/","menu\_id":3803,"has\_children":false},{"label":"Publications","id":"menu-item-54326","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-54326","url":"\/publications\/","menu\_id":54326,"has\_children":true,"menu\_items":[{"label":"Search All Publications","id":"menu-item-54327","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-54327","url":"\/publications\/","menu\_id":54327,"has\_children":false},{"label":"Books","id":"menu-item-54329","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-54329","url":"\/publications\/?page=1&tax\_and\_terms=197","menu\_id":54329,"has\_children":false},{"label":"Journal Articles","id":"menu-item-54330","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-54330","url":"\/publications\/?page=1&tax\_and\_terms=205","menu\_id":54330,"has\_children":false},{"label":"Briefs","id":"menu-item-54331","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-54331","url":"\/publications\/?page=1&tax\_and\_terms=329","menu\_id":54331,"has\_children":false},{"label":"Working Papers","id":"menu-item-54332","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-54332","url":"\/publications\/?page=1&tax\_and\_terms=325","menu\_id":54332,"has\_children":false},{"label":"Student Journals","id":"menu-item-54328","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-54328","url":"\/organizations\/?page=1&tax\_and\_terms=311","menu\_id":54328,"has\_children":false},{"label":"Dissertations &#038; Thesis","id":"menu-item-54333","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-54333","url":"\/publications\/?page=1&tax\_and\_terms=334","menu\_id":54333,"has\_children":false}]},{"label":"Faculty Research","id":"menu-item-3804","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-3804","url":"https:\/\/law.stanford.edu\/research\/faculty-research\/","menu\_id":3804,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-350267","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-350267","url":"https:\/\/law.stanford.edu\/research\/faculty-research\/","menu\_id":350267,"has\_children":false},{"label":"Faculty Book Series","id":"menu-item-385605","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-385605","url":"https:\/\/law.stanford.edu\/research\/faculty-research\/faculty-book-series\/","menu\_id":385605,"has\_children":false}]},{"label":"SLS Fellowships","id":"menu-item-207548","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-207548","url":"https:\/\/law.stanford.edu\/research\/sls-fellowships\/","menu\_id":207548,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-398408","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-398408","url":"https:\/\/law.stanford.edu\/research\/sls-fellowships\/","menu\_id":398408,"has\_children":false},{"label":"Corporate Governance and Practice Teaching Fellowship","id":"menu-item-491015","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-491015","url":"https:\/\/law.stanford.edu\/research\/sls-fellowships\/corporate-governance-and-practice-teaching-fellowship\/","menu\_id":491015,"has\_children":false},{"label":"Stanford Law School Empirical Research Fellowship","id":"menu-item-350465","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-350465","url":"https:\/\/law.stanford.edu\/research\/sls-fellowships\/empirical-research-fellowship\/","menu\_id":350465,"has\_children":false},{"label":"Thomas C. Grey Fellowship","id":"menu-item-438360","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-438360","url":"https:\/\/law.stanford.edu\/research\/sls-fellowships\/thomas-c-grey-fellowship\/","menu\_id":438360,"has\_children":false}]},{"label":"Robert Crown Law Library","id":"menu-item-3807","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-3807","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/","menu\_id":3807,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-5271","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-5271","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/","menu\_id":5271,"has\_children":false},{"label":"RCLL Access Policies","id":"menu-item-28611","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-28611","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/access-policies\/","menu\_id":28611,"has\_children":false},{"label":"Alumni Services","id":"menu-item-221875","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-221875","url":"https:\/\/law.stanford.edu\/i-am-an-alum\/contact-us\/sls-alumnialumnae-services\/","menu\_id":221875,"has\_children":false},{"label":"Faculty Services","id":"menu-item-37120","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-37120","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/faculty-services\/","menu\_id":37120,"has\_children":false},{"label":"Frequently Used Services","id":"menu-item-221877","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-221877","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/#slsnav-frequently-used-services","menu\_id":221877,"has\_children":false},{"label":"Special Collections","id":"menu-item-325566","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-325566","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/rcll-special-collections\/","menu\_id":325566,"has\_children":false},{"label":"Hours","id":"menu-item-28648","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-28648","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/hours\/","menu\_id":28648,"has\_children":false},{"label":"Research Guides","id":"menu-item-221879","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-221879","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/research-guides\/","menu\_id":221879,"has\_children":false},{"label":"Student Services","id":"menu-item-221880","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-221880","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/student-services\/","menu\_id":221880,"has\_children":false},{"label":"About the Law Library","id":"menu-item-157539","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-157539","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/about-the-law-library\/","menu\_id":157539,"has\_children":false}]},{"label":"Faculty Directory","id":"menu-item-306257","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-306257","url":"https:\/\/law.stanford.edu\/directory\/?tax\_and\_terms=1067&page=1","menu\_id":306257,"has\_children":false}]},{"label":"News &#038; Media","id":"menu-item-5235","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5235","url":"https:\/\/law.stanford.edu\/media\/","menu\_id":5235,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-3810","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-3810","url":"https:\/\/law.stanford.edu\/media\/","menu\_id":3810,"has\_children":false},{"label":"SLS News &#038; Announcements","id":"menu-item-55815","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-55815","url":"\/press\/?tax\_and\_terms=194&page=1","menu\_id":55815,"has\_children":false},{"label":"Media Coverage","id":"menu-item-55794","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-55794","url":"\/press\/?tax\_and\_terms=193&page=1","menu\_id":55794,"has\_children":false},{"label":"Op-Eds","id":"menu-item-55826","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-55826","url":"\/publications\/?tax\_and\_terms=326&page=1","menu\_id":55826,"has\_children":false},{"label":"SLS Blogs","id":"menu-item-119527","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-119527","url":"\/blog\/","menu\_id":119527,"has\_children":true,"menu\_items":[{"label":"All SLS Blogs","id":"menu-item-119582","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-119582","url":"\/blog\/","menu\_id":119582,"has\_children":false},{"label":"Deborah L. Rhode Center on the Legal Profession","id":"menu-item-119532","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-119532","url":"\/blog\/?tax\_and\_terms=6768&page=1","menu\_id":119532,"has\_children":false},{"label":"Center for Internet and Society","id":"menu-item-136728","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-136728","url":"https:\/\/cyberlaw.stanford.edu\/blog","menu\_id":136728,"has\_children":false},{"label":"CodeX","id":"menu-item-161292","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-161292","url":"https:\/\/law.stanford.edu\/blog\/?tax\_and\_terms=3520&page=1","menu\_id":161292,"has\_children":false},{"label":"Environmental and Natural Resources Law &#038; Policy Program","id":"menu-item-562293","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-562293","url":"\/blog\/?tax\_and\_terms=8866&page=1","menu\_id":562293,"has\_children":false},{"label":"The \"Fayemous\" SLS Admissions Blog","id":"menu-item-119530","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-119530","url":"\/blog\/?page=1&tax\_and\_terms=3137","menu\_id":119530,"has\_children":false},{"label":"Law and Biosciences Blog","id":"menu-item-119534","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-119534","url":"\/blog\/?page=1&tax\_and\_terms=3140","menu\_id":119534,"has\_children":false},{"label":"Law and Policy Lab","id":"menu-item-119535","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-119535","url":"\/blog\/?page=1&tax\_and\_terms=3141","menu\_id":119535,"has\_children":false},{"label":"The Legal Aggregate","id":"menu-item-119747","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-119747","url":"\/legal-aggregate\/","menu\_id":119747,"has\_children":false},{"label":"Mills Legal Clinic of Stanford Law School","id":"menu-item-119537","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-119537","url":"\/blog\/?page=1&tax\_and\_terms=3149","menu\_id":119537,"has\_children":false},{"label":"Stanford Center for Racial Justice","id":"menu-item-411726","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-411726","url":"\/blog\/?tax\_and\_terms=7738&page=1","menu\_id":411726,"has\_children":false},{"label":"Stanford Securities Litigation Analytics","id":"menu-item-119540","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-119540","url":"\/blog\/?page=1&tax\_and\_terms=3160","menu\_id":119540,"has\_children":false}]},{"label":"Stanford Legal","id":"menu-item-227612","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-227612","url":"https:\/\/law.stanford.edu\/stanford-legal-podcast\/","menu\_id":227612,"has\_children":true,"menu\_items":[{"label":"Stanford Legal","id":"menu-item-339185","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-339185","url":"https:\/\/law.stanford.edu\/stanford-legal-podcast\/","menu\_id":339185,"has\_children":false},{"label":"Archive","id":"menu-item-339184","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-339184","url":"https:\/\/law.stanford.edu\/podcasts\/?tax\_and\_terms=7608&page=1","menu\_id":339184,"has\_children":false}]},{"label":"Video Center","id":"menu-item-37155","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-37155","url":"https:\/\/law.stanford.edu\/media\/video-center\/","menu\_id":37155,"has\_children":false},{"label":"Social Media Hub","id":"menu-item-3811","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-3811","url":"https:\/\/law.stanford.edu\/social-media\/","menu\_id":3811,"has\_children":false},{"label":"Stanford Lawyer Magazine","id":"menu-item-116767","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-116767","url":"https:\/\/law.stanford.edu\/stanford-lawyer-magazine\/","menu\_id":116767,"has\_children":true,"menu\_items":[{"label":"Current Issue","id":"menu-item-202453","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-202453","url":"https:\/\/law.stanford.edu\/stanford-lawyer-magazine\/","menu\_id":202453,"has\_children":false},{"label":"Back Issues","id":"menu-item-200555","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-200555","url":"https:\/\/law.stanford.edu\/stanford-lawyer\/","menu\_id":200555,"has\_children":false},{"label":"Legal Aggregate","id":"menu-item-200556","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-200556","url":"https:\/\/law.stanford.edu\/legal-aggregate\/","menu\_id":200556,"has\_children":false}]},{"label":"SLS Newsletters","id":"menu-item-37177","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-37177","url":"https:\/\/law.stanford.edu\/media\/sls-newsletters\/","menu\_id":37177,"has\_children":false},{"label":"For Journalists","id":"menu-item-62158","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-62158","url":"https:\/\/law.stanford.edu\/i-am-a-journalist\/","menu\_id":62158,"has\_children":false}]},{"label":"Programs &#038; Centers","id":"menu-item-76153","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-76153","url":"https:\/\/law.stanford.edu\/programs-centers-and-projects\/","menu\_id":76153,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-76160","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-76160","url":"https:\/\/law.stanford.edu\/programs-centers-and-projects\/","menu\_id":76160,"has\_children":false},{"label":"Directory","id":"menu-item-76162","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-76162","url":"\/organizations\/?page=1&tax\_and\_terms=307","menu\_id":76162,"has\_children":false}]},{"label":"Community","id":"menu-item-5244","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5244","url":"https:\/\/law.stanford.edu\/community\/","menu\_id":5244,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-5243","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-5243","url":"https:\/\/law.stanford.edu\/community\/","menu\_id":5243,"has\_children":false},{"label":"Student Life","id":"menu-item-5242","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5242","url":"https:\/\/law.stanford.edu\/community\/student-life\/","menu\_id":5242,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-5273","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-5273","url":"https:\/\/law.stanford.edu\/community\/student-life\/","menu\_id":5273,"has\_children":false},{"label":"Student Organizations","id":"menu-item-58838","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58838","url":"\/organizations\/?page=1&tax\_and\_terms=308","menu\_id":58838,"has\_children":false},{"label":"Student Journals","id":"menu-item-58839","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58839","url":"\/organizations\/?page=1&tax\_and\_terms=311","menu\_id":58839,"has\_children":false},{"label":"Housing","id":"menu-item-58855","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-58855","url":"https:\/\/law.stanford.edu\/community\/student-life\/housing\/","menu\_id":58855,"has\_children":false},{"label":"Graduate Life Office","id":"menu-item-54335","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-54335","url":"https:\/\/glo.stanford.edu\/","menu\_id":54335,"has\_children":false},{"label":"Diploma Ceremony Logistics 2026","id":"menu-item-553829","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-553829","url":"https:\/\/law.stanford.edu\/community\/student-life\/getting-ready-graduation\/","menu\_id":553829,"has\_children":false},{"label":"Past Graduations","id":"menu-item-205087","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-205087","url":"https:\/\/law.stanford.edu\/past-graduations\/","menu\_id":205087,"has\_children":false}]},{"label":"Alumni Life","id":"menu-item-397489","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-397489","url":"https:\/\/law.stanford.edu\/i-am-an-alum\/","menu\_id":397489,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-209014","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-209014","url":"https:\/\/law.stanford.edu\/i-am-an-alum\/","menu\_id":209014,"has\_children":false},{"label":"Alumni Communities","id":"menu-item-58843","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58843","url":"\/i-am-an-alum\/alumni-communities\/","menu\_id":58843,"has\_children":false},{"label":"Alumni Directory","id":"menu-item-58854","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58854","url":"https:\/\/alumni-law.stanford.edu\/get\/page\/login?pg=yes&am=tpartyFA&nu=https:\*\*alumni-law.stanford.edu\/get\/page\/directory\/search\/","menu\_id":58854,"has\_children":false},{"label":"Past Graduations","id":"menu-item-82088","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-82088","url":"https:\/\/law.stanford.edu\/past-graduations\/","menu\_id":82088,"has\_children":false}]},{"label":"Clinics","id":"menu-item-58840","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58840","url":"https:\/\/law.stanford.edu\/organizations\/?tax\_and\_terms=304&page=1","menu\_id":58840,"has\_children":false},{"label":"Programs &#038; Centers","id":"menu-item-58841","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58841","url":"https:\/\/law.stanford.edu\/organizations\/?page=1&tax\_and\_terms=307","menu\_id":58841,"has\_children":false},{"label":"Projects","id":"menu-item-288122","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-288122","url":"https:\/\/law.stanford.edu\/organizations\/?page=1&tax\_and\_terms=3812","menu\_id":288122,"has\_children":false},{"label":"Administrative Offices","id":"menu-item-58842","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58842","url":"https:\/\/law.stanford.edu\/organizations\/?tax\_and\_terms=305&page=1","menu\_id":58842,"has\_children":false},{"label":"People","id":"menu-item-58846","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-58846","url":"\/directory\/","menu\_id":58846,"has\_children":true,"menu\_items":[{"label":"Faculty","id":"menu-item-58848","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58848","url":"\/directory\/?tax\_and\_terms=1067&page=1","menu\_id":58848,"has\_children":false},{"label":"Deans &#038; Administrators","id":"menu-item-127290","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-127290","url":"\/directory\/?tax\_and\_terms=1074&page=1","menu\_id":127290,"has\_children":false},{"label":"Lecturers","id":"menu-item-58850","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58850","url":"\/directory\/?tax\_and\_terms=1083&page=1","menu\_id":58850,"has\_children":false},{"label":"Visiting &#038; Affiliated Faculty","id":"menu-item-58852","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58852","url":"\/directory\/?tax\_and\_terms=1087&page=1","menu\_id":58852,"has\_children":false},{"label":"Academic &#038; Research Fellows","id":"menu-item-58851","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58851","url":"\/directory\/?tax\_and\_terms=1064&page=1","menu\_id":58851,"has\_children":false},{"label":"Students","id":"menu-item-58853","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58853","url":"\/directory\/?tax\_and\_terms=1095&page=1","menu\_id":58853,"has\_children":false},{"label":"Staff","id":"menu-item-58849","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58849","url":"\/directory\/?tax\_and\_terms=1085&page=1","menu\_id":58849,"has\_children":false},{"label":"Full Directory","id":"menu-item-58847","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-58847","url":"\/directory\/","menu\_id":58847,"has\_children":false}]}]},{"label":"Careers","id":"menu-item-5253","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5253","url":"https:\/\/law.stanford.edu\/careers\/","menu\_id":5253,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-5254","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-5254","url":"https:\/\/law.stanford.edu\/careers\/","menu\_id":5254,"has\_children":false},{"label":"Career Possibilities","id":"menu-item-28668","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-28668","url":"https:\/\/law.stanford.edu\/careers\/career-possibilities\/","menu\_id":28668,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-28669","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-28669","url":"https:\/\/law.stanford.edu\/careers\/career-possibilities\/","menu\_id":28669,"has\_children":false},{"label":"Academia","id":"menu-item-28670","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-28670","url":"https:\/\/law.stanford.edu\/careers\/career-possibilities\/academia\/","menu\_id":28670,"has\_children":false},{"label":"Public Interest and Government","id":"menu-item-61004","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-61004","url":"https:\/\/law.stanford.edu\/levin-center\/careers\/","menu\_id":61004,"has\_children":false},{"label":"Private Sector","id":"menu-item-80837","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80837","url":"https:\/\/law.stanford.edu\/careers\/career-possibilities\/private-sector\/","menu\_id":80837,"has\_children":false},{"label":"Judicial Clerkships","id":"menu-item-80840","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-80840","url":"https:\/\/law.stanford.edu\/careers\/career-possibilities\/judicial-clerkships\/","menu\_id":80840,"has\_children":false},{"label":"Non-Law","id":"menu-item-80838","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80838","url":"https:\/\/law.stanford.edu\/careers\/career-possibilities\/non-law\/","menu\_id":80838,"has\_children":false}]},{"label":"Counseling and Assessments","id":"menu-item-5256","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5256","url":"https:\/\/law.stanford.edu\/careers\/counseling-assessments\/","menu\_id":5256,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-5280","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-5280","url":"https:\/\/law.stanford.edu\/careers\/counseling-assessments\/","menu\_id":5280,"has\_children":false},{"label":"Assessments &amp; Practice Areas","id":"menu-item-28023","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-28023","url":"https:\/\/law.stanford.edu\/careers\/counseling-assessments\/assessments\/","menu\_id":28023,"has\_children":false},{"label":"Private Sector Advisors","id":"menu-item-28024","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-28024","url":"https:\/\/law.stanford.edu\/careers\/counseling-assessments\/private-sector-advisors\/","menu\_id":28024,"has\_children":false},{"label":"Public Sector Advisors","id":"menu-item-114063","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-114063","url":"\/levin-center\/#slsnav-contacts","menu\_id":114063,"has\_children":false}]},{"label":"Employer Research Tools","id":"menu-item-5257","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-5257","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/","menu\_id":5257,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-5281","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-5281","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/","menu\_id":5281,"has\_children":false},{"label":"Legal Directories","id":"menu-item-80845","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80845","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/legal-directories\/","menu\_id":80845,"has\_children":false},{"label":"Law Firms: Practice Area, Culture, &amp; Location","id":"menu-item-80846","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80846","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/surveys-and-rankings\/","menu\_id":80846,"has\_children":false},{"label":"Public Interest and Plaintiffs\u2019 Law Firms","id":"menu-item-80849","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80849","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/public-interest-law-firms\/","menu\_id":80849,"has\_children":false},{"label":"In-House Resources","id":"menu-item-80844","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80844","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/in-house-resources\/","menu\_id":80844,"has\_children":false},{"label":"Student Employment &amp; Contact Lists","id":"menu-item-80850","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80850","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/student-employment-contact-lists\/","menu\_id":80850,"has\_children":false},{"label":"Law Blawgs","id":"menu-item-114065","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-114065","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/law-blawgs\/","menu\_id":114065,"has\_children":false}]},{"label":"Getting the Job","id":"menu-item-82043","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-82043","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/","menu\_id":82043,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-82042","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-82042","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/","menu\_id":82042,"has\_children":false},{"label":"Job Search Timeline","id":"menu-item-114069","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-114069","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/job-search-timeline\/","menu\_id":114069,"has\_children":false},{"label":"Researching Employers","id":"menu-item-127322","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-127322","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/researching-employers\/","menu\_id":127322,"has\_children":false},{"label":"Preparing Your Application Materials","id":"menu-item-127301","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-127301","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/preparing-your-application-materials\/","menu\_id":127301,"has\_children":false},{"label":"Sample Application Materials","id":"menu-item-80851","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80851","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/sample-application-materials\/","menu\_id":80851,"has\_children":false},{"label":"Networking","id":"menu-item-80855","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80855","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/networking\/","menu\_id":80855,"has\_children":false},{"label":"Interviewing","id":"menu-item-80857","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80857","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/interviewing\/","menu\_id":80857,"has\_children":false},{"label":"Callbacks &amp; Offers","id":"menu-item-80854","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80854","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/callbacks-offers\/","menu\_id":80854,"has\_children":false},{"label":"Nondiscrimination Policy","id":"menu-item-264275","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-264275","url":"https:\/\/law.stanford.edu\/careers\/online-coordinated-interviews\/non-discrimination-policy\/","menu\_id":264275,"has\_children":false}]},{"label":"Online Coordinated Interviews (OCI)","id":"menu-item-80853","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-80853","url":"https:\/\/law.stanford.edu\/careers\/online-coordinated-interviews\/","menu\_id":80853,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-82157","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-82157","url":"https:\/\/law.stanford.edu\/careers\/online-coordinated-interviews\/","menu\_id":82157,"has\_children":false},{"label":"Frequently Asked Questions","id":"menu-item-128285","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-128285","url":"https:\/\/law.stanford.edu\/careers\/online-coordinated-interviews\/frequently-asked-questions\/","menu\_id":128285,"has\_children":false},{"label":"OCI Logistics","id":"menu-item-127298","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-127298","url":"https:\/\/law.stanford.edu\/careers\/online-coordinated-interviews\/oci-logistics\/","menu\_id":127298,"has\_children":false},{"label":"OCI Bidding &#038; Strategy","id":"menu-item-80878","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80878","url":"https:\/\/law.stanford.edu\/careers\/online-coordinated-interviews\/bidding-strategy\/","menu\_id":80878,"has\_children":false},{"label":"Nondiscrimination Policy","id":"menu-item-80905","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80905","url":"https:\/\/law.stanford.edu\/careers\/online-coordinated-interviews\/non-discrimination-policy\/","menu\_id":80905,"has\_children":false}]},{"label":"Employment Outcomes","id":"menu-item-82046","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-82046","url":"https:\/\/law.stanford.edu\/careers\/employment-outcomes\/","menu\_id":82046,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-82047","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-82047","url":"https:\/\/law.stanford.edu\/careers\/employment-outcomes\/","menu\_id":82047,"has\_children":false},{"label":"Graduate Employment Outcomes","id":"menu-item-80873","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80873","url":"https:\/\/law.stanford.edu\/careers\/employment-outcomes\/graduate-employment-outcomes\/","menu\_id":80873,"has\_children":false},{"label":"1L &amp; 2L Employment Outcomes","id":"menu-item-80874","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-80874","url":"https:\/\/law.stanford.edu\/careers\/employment-outcomes\/1l-2l-employment-outcomes\/","menu\_id":80874,"has\_children":false}]},{"label":"1L OCS Resources","id":"menu-item-317916","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-317916","url":"https:\/\/law.stanford.edu\/careers\/1l-introduction-to-ocs-website-tools\/","menu\_id":317916,"has\_children":false},{"label":"Summer Associate Resources","id":"menu-item-367262","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-367262","url":"https:\/\/law.stanford.edu\/careers\/summer-associate-resources\/","menu\_id":367262,"has\_children":false},{"label":"Advanced Degree Students","id":"menu-item-80839","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-80839","url":"https:\/\/law.stanford.edu\/careers\/advanced-degree-students\/","menu\_id":80839,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-127374","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-127374","url":"https:\/\/law.stanford.edu\/careers\/advanced-degree-students\/","menu\_id":127374,"has\_children":false},{"label":"Getting Started","id":"menu-item-438742","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-438742","url":"https:\/\/law.stanford.edu\/careers\/advanced-degree-students\/getting-started\/","menu\_id":438742,"has\_children":false},{"label":"Self-Assessments","id":"menu-item-438743","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-438743","url":"https:\/\/law.stanford.edu\/careers\/counseling-assessments\/assessments\/","menu\_id":438743,"has\_children":false},{"label":"Research Tools","id":"menu-item-128056","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-128056","url":"https:\/\/law.stanford.edu\/careers\/employer-research-tools\/","menu\_id":128056,"has\_children":false},{"label":"Building Your Network","id":"menu-item-127308","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-127308","url":"https:\/\/law.stanford.edu\/careers\/advanced-degree-students\/networking\/","menu\_id":127308,"has\_children":false},{"label":"Job Application Resources","id":"menu-item-127305","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-127305","url":"https:\/\/law.stanford.edu\/careers\/advanced-degree-students\/job-application-resources\/","menu\_id":127305,"has\_children":false},{"label":"Career Resources","id":"menu-item-127304","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-127304","url":"https:\/\/law.stanford.edu\/careers\/advanced-degree-students\/career-resources\/","menu\_id":127304,"has\_children":false},{"label":"Interviewing","id":"menu-item-128059","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-128059","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/interviewing\/","menu\_id":128059,"has\_children":false},{"label":"Workshop Recordings &#038; Resources","id":"menu-item-346367","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-346367","url":"https:\/\/law.stanford.edu\/advanced-degree-presentation-recordings-and-resources\/","menu\_id":346367,"has\_children":false}]},{"label":"Alumni Career Resources","id":"menu-item-132957","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-has-children menu-item-132957","url":"https:\/\/law.stanford.edu\/careers\/alumni-career-resources\/","menu\_id":132957,"has\_children":true,"menu\_items":[{"label":"Overview","id":"menu-item-133228","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-133228","url":"https:\/\/law.stanford.edu\/careers\/alumni-career-resources\/","menu\_id":133228,"has\_children":false},{"label":"Private Sector Advising","id":"menu-item-132964","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-132964","url":"https:\/\/law.stanford.edu\/careers\/counseling-assessments\/private-sector-advisors\/","menu\_id":132964,"has\_children":false},{"label":"Job Postings","id":"menu-item-132963","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-132963","url":"https:\/\/law.stanford.edu\/careers\/alumni-career-resources\/alumni-job-postings\/","menu\_id":132963,"has\_children":false},{"label":"Judicial Clerkships","id":"menu-item-132965","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-132965","url":"https:\/\/law.stanford.edu\/careers\/career-possibilities\/judicial-clerkships\/alumni-applicants\/","menu\_id":132965,"has\_children":false},{"label":"Legal Recruiters &amp; Staffing Agencies","id":"menu-item-132962","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-132962","url":"https:\/\/law.stanford.edu\/careers\/alumni-career-resources\/legal-recruiters-staffing-agencies\/","menu\_id":132962,"has\_children":false},{"label":"Compensation Resources","id":"menu-item-132961","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-132961","url":"https:\/\/law.stanford.edu\/careers\/alumni-career-resources\/compensation-resources\/","menu\_id":132961,"has\_children":false},{"label":"Job Search Tools","id":"menu-item-132960","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-132960","url":"https:\/\/law.stanford.edu\/careers\/alumni-career-resources\/job-search-tools\/","menu\_id":132960,"has\_children":false},{"label":"Sample Lateral Application Materials","id":"menu-item-132959","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-132959","url":"https:\/\/law.stanford.edu\/careers\/alumni-career-resources\/sample-lateral-application-materials\/","menu\_id":132959,"has\_children":false},{"label":"Preparing for Your Interview","id":"menu-item-132958","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-132958","url":"https:\/\/law.stanford.edu\/careers\/alumni-career-resources\/preparing-for-your-interview\/","menu\_id":132958,"has\_children":false},{"label":"Networking","id":"menu-item-132966","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-132966","url":"https:\/\/law.stanford.edu\/careers\/getting-the-job\/networking\/","menu\_id":132966,"has\_children":false}]},{"label":"Symplicity for Students","id":"menu-item-5261","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-5261","url":"https:\/\/law-stanford-csm.symplicity.com\/students\/","menu\_id":5261,"has\_children":false},{"label":"Recruiting Policies","id":"menu-item-362881","classes":" menu-item menu-item-type-post\_type menu-item-object-page menu-item-362881","url":"https:\/\/law.stanford.edu\/i-am-an-employer\/recruiting-policies\/","menu\_id":362881,"has\_children":false}]}]} 

{"menu\_items":[{"label":"Event Calendar","id":"menu-item-38539","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-38539","url":"\/events\/","menu\_id":38539,"has\_children":false},{"label":"Archived Events","id":"menu-item-38542","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-38542","url":"\/events-archive\/","menu\_id":38542,"has\_children":false},{"label":"Faculty Directory","id":"menu-item-38540","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-38540","url":"\/directory\/?tax\_and\_terms=1067&page=1","menu\_id":38540,"has\_children":false},{"label":"Full Directory","id":"menu-item-161023","classes":" menu-item menu-item-type-custom menu-item-object-custom menu-item-161023","url":"\/directory\/","menu\_id":161023,"has\_children":false},{"label":"Law Library","id":"menu-item-120725","classes":" menu-item menu-item-type-post\_type menu-item-object-organization menu-item-120725","url":"https:\/\/law.stanford.edu\/robert-crown-law-library\/","menu\_id":120725,"has\_children":false}]} 
(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.\_\_CF$cv$params={r:'9f79701e9a42590b',t:'MTc3ODA4NTc0NA=='};var a=document.createElement('script');a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();
