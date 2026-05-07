# Aditya — The Dark Factory: Engineering Teams That Run With the Lights Off

Source: https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/

---

var wpcom\_remote\_login\_extra\_auth = '';
function wpcom\_remote\_login\_remove\_dom\_node\_id( element\_id ) {
var dom\_node = document.getElementById( element\_id );
if ( dom\_node ) { dom\_node.parentNode.removeChild( dom\_node ); }
}
function wpcom\_remote\_login\_remove\_dom\_node\_classes( class\_name ) {
var dom\_nodes = document.querySelectorAll( '.' + class\_name );
for ( var i = 0; i < dom\_nodes.length; i++ ) {
dom\_nodes[ i ].parentNode.removeChild( dom\_nodes[ i ] );
}
}
function wpcom\_remote\_login\_final\_cleanup() {
wpcom\_remote\_login\_remove\_dom\_node\_classes( "wpcom\_remote\_login\_msg" );
wpcom\_remote\_login\_remove\_dom\_node\_id( "wpcom\_remote\_login\_key" );
wpcom\_remote\_login\_remove\_dom\_node\_id( "wpcom\_remote\_login\_validate" );
wpcom\_remote\_login\_remove\_dom\_node\_id( "wpcom\_remote\_login\_js" );
wpcom\_remote\_login\_remove\_dom\_node\_id( "wpcom\_request\_access\_iframe" );
wpcom\_remote\_login\_remove\_dom\_node\_id( "wpcom\_request\_access\_styles" );
}
// Watch for messages back from the remote login
window.addEventListener( "message", function( e ) {
if ( e.origin === "https://r-login.wordpress.com" ) {
var data = {};
try {
data = JSON.parse( e.data );
} catch( e ) {
wpcom\_remote\_login\_final\_cleanup();
return;
}
if ( data.msg === 'LOGIN' ) {
// Clean up the login check iframe
wpcom\_remote\_login\_remove\_dom\_node\_id( "wpcom\_remote\_login\_key" );
var id\_regex = new RegExp( /^[0-9]+$/ );
var token\_regex = new RegExp( /^.\*|.\*|.\*$/ );
if (
token\_regex.test( data.token )
&& id\_regex.test( data.wpcomid )
) {
// We have everything we need to ask for a login
var script = document.createElement( "script" );
script.setAttribute( "id", "wpcom\_remote\_login\_validate" );
script.src = '/remote-login.php?wpcom\_remote\_login=validate'
+ '&wpcomid=' + data.wpcomid
+ '&token=' + encodeURIComponent( data.token )
+ '&host=' + window.location.protocol
+ '//' + window.location.hostname
+ '&postid=7826'
+ '&is\_singular=1';
document.body.appendChild( script );
}
return;
}
// Safari ITP, not logged in, so redirect
if ( data.msg === 'LOGIN-REDIRECT' ) {
window.location = 'https://wordpress.com/log-in?redirect\_to=' + window.location.href;
return;
}
// Safari ITP, storage access failed, remove the request
if ( data.msg === 'LOGIN-REMOVE' ) {
var css\_zap = 'html { -webkit-transition: margin-top 1s; transition: margin-top 1s; } /\* 9001 \*/ html { margin-top: 0 !important; } \* html body { margin-top: 0 !important; } @media screen and ( max-width: 782px ) { html { margin-top: 0 !important; } \* html body { margin-top: 0 !important; } }';
var style\_zap = document.createElement( 'style' );
style\_zap.type = 'text/css';
style\_zap.appendChild( document.createTextNode( css\_zap ) );
document.body.appendChild( style\_zap );
var e = document.getElementById( 'wpcom\_request\_access\_iframe' );
e.parentNode.removeChild( e );
document.cookie = 'wordpress\_com\_login\_access=denied; path=/; max-age=31536000';
return;
}
// Safari ITP
if ( data.msg === 'REQUEST\_ACCESS' ) {
console.log( 'request access: safari' );
// Check ITP iframe enable/disable knob
if ( wpcom\_remote\_login\_extra\_auth !== 'safari\_itp\_iframe' ) {
return;
}
// If we are in a "private window" there is no ITP.
var private\_window = false;
try {
var opendb = window.openDatabase( null, null, null, null );
} catch( e ) {
private\_window = true;
}
if ( private\_window ) {
console.log( 'private window' );
return;
}
var iframe = document.createElement( 'iframe' );
iframe.id = 'wpcom\_request\_access\_iframe';
iframe.setAttribute( 'scrolling', 'no' );
iframe.setAttribute( 'sandbox', 'allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-top-navigation-by-user-activation' );
iframe.src = 'https://r-login.wordpress.com/remote-login.php?wpcom\_remote\_login=request\_access&origin=' + encodeURIComponent( data.origin ) + '&wpcomid=' + encodeURIComponent( data.wpcomid );
var css = 'html { -webkit-transition: margin-top 1s; transition: margin-top 1s; } /\* 9001 \*/ html { margin-top: 46px !important; } \* html body { margin-top: 46px !important; } @media screen and ( max-width: 660px ) { html { margin-top: 71px !important; } \* html body { margin-top: 71px !important; } #wpcom\_request\_access\_iframe { display: block; height: 71px !important; } } #wpcom\_request\_access\_iframe { border: 0px; height: 46px; position: fixed; top: 0; left: 0; width: 100%; min-width: 100%; z-index: 99999; background: #23282d; } ';
var style = document.createElement( 'style' );
style.type = 'text/css';
style.id = 'wpcom\_request\_access\_styles';
style.appendChild( document.createTextNode( css ) );
document.body.appendChild( style );
document.body.appendChild( iframe );
}
if ( data.msg === 'DONE' ) {
wpcom\_remote\_login\_final\_cleanup();
}
}
}, false );
// Inject the remote login iframe after the page has had a chance to load
// more critical resources
window.addEventListener( "DOMContentLoaded", function( e ) {
var iframe = document.createElement( "iframe" );
iframe.style.display = "none";
iframe.setAttribute( "scrolling", "no" );
iframe.setAttribute( "id", "wpcom\_remote\_login\_key" );
iframe.src = "https://r-login.wordpress.com/remote-login.php"
+ "?wpcom\_remote\_login=key"
+ "&origin=aHR0cHM6Ly9hYmFkaXR5YS5jb20%3D"
+ "&wpcomid=62550"
+ "&time=" + Math.floor( Date.now() / 1000 );
document.body.appendChild( iframe );
}, false );
The Dark Factory: Engineering Teams That Run With the Lights Off – AB's Reflections






/\* <![CDATA[ \*/
function addLoadEvent(func) {
var oldonload = window.onload;
if (typeof window.onload != 'function') {
window.onload = func;
} else {
window.onload = function () {
oldonload();
func();
}
}
}
/\* ]]> \*/


.wp-block-site-title{box-sizing:border-box}.wp-block-site-title :where(a){color:inherit;font-family:inherit;font-size:inherit;font-style:inherit;font-weight:inherit;letter-spacing:inherit;line-height:inherit;text-decoration:inherit}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/site-title/style.min.css \*/

.wp-block-navigation .wp-block-page-list{align-items:var(--navigation-layout-align,initial);background-color:inherit;display:flex;flex-direction:var(--navigation-layout-direction,initial);flex-wrap:var(--navigation-layout-wrap,wrap);justify-content:var(--navigation-layout-justify,initial)}.wp-block-navigation .wp-block-navigation-item{background-color:inherit}.wp-block-page-list{box-sizing:border-box}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/page-list/style.min.css \*/

.is-style-compact .is-not-subscriber .wp-block-button\_\_link,.is-style-compact .is-not-subscriber .wp-block-jetpack-subscriptions\_\_button{border-end-start-radius:0!important;border-start-start-radius:0!important;margin-inline-start:0!important}.is-style-compact .is-not-subscriber .components-text-control\_\_input,.is-style-compact .is-not-subscriber p#subscribe-email input[type=email]{border-end-end-radius:0!important;border-start-end-radius:0!important}.is-style-compact:not(.wp-block-jetpack-subscriptions\_\_use-newline) .components-text-control\_\_input{border-inline-end-width:0!important}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form-container{display:flex;flex-direction:column}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline:not(.wp-block-jetpack-subscriptions\_\_use-newline) .is-not-subscriber .wp-block-jetpack-subscriptions\_\_form-elements{align-items:flex-start;display:flex}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline:not(.wp-block-jetpack-subscriptions\_\_use-newline) p#subscribe-submit{display:flex;justify-content:center}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form .wp-block-jetpack-subscriptions\_\_button,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form .wp-block-jetpack-subscriptions\_\_textfield .components-text-control\_\_input,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form button,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form input[type=email],.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form .wp-block-jetpack-subscriptions\_\_button,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form .wp-block-jetpack-subscriptions\_\_textfield .components-text-control\_\_input,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form button,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form input[type=email]{box-sizing:border-box;cursor:pointer;line-height:1.3;min-width:auto!important;white-space:nowrap!important}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form input[type=email]::placeholder,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form input[type=email]:disabled,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form input[type=email]::placeholder,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form input[type=email]:disabled{color:currentColor;opacity:.5}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form .wp-block-jetpack-subscriptions\_\_button,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form button,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form .wp-block-jetpack-subscriptions\_\_button,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form button{border-color:#0000;border-style:solid}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form .wp-block-jetpack-subscriptions\_\_textfield,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form p#subscribe-email,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form .wp-block-jetpack-subscriptions\_\_textfield,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form p#subscribe-email{background:#0000;flex-grow:1}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form .wp-block-jetpack-subscriptions\_\_textfield .components-base-control\_\_field,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form .wp-block-jetpack-subscriptions\_\_textfield .components-text-control\_\_input,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form .wp-block-jetpack-subscriptions\_\_textfield input[type=email],.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form p#subscribe-email .components-base-control\_\_field,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form p#subscribe-email .components-text-control\_\_input,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form p#subscribe-email input[type=email],.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form .wp-block-jetpack-subscriptions\_\_textfield .components-base-control\_\_field,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form .wp-block-jetpack-subscriptions\_\_textfield .components-text-control\_\_input,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form .wp-block-jetpack-subscriptions\_\_textfield input[type=email],.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form p#subscribe-email .components-base-control\_\_field,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form p#subscribe-email .components-text-control\_\_input,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form p#subscribe-email input[type=email]{height:auto;margin:0;width:100%}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form p#subscribe-email,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline .wp-block-jetpack-subscriptions\_\_form p#subscribe-submit,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form p#subscribe-email,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline form p#subscribe-submit{line-height:0;margin:0;padding:0}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline.wp-block-jetpack-subscriptions\_\_show-subs .wp-block-jetpack-subscriptions\_\_subscount{font-size:16px;margin:8px 0;text-align:end}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline.wp-block-jetpack-subscriptions\_\_use-newline .wp-block-jetpack-subscriptions\_\_form-elements{display:block}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline.wp-block-jetpack-subscriptions\_\_use-newline .wp-block-jetpack-subscriptions\_\_button,.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline.wp-block-jetpack-subscriptions\_\_use-newline button{display:inline-block;max-width:100%}.wp-block-jetpack-subscriptions.wp-block-jetpack-subscriptions\_\_supports-newline.wp-block-jetpack-subscriptions\_\_use-newline .wp-block-jetpack-subscriptions\_\_subscount{text-align:start}#subscribe-submit.is-link{text-align:center;width:auto!important}#subscribe-submit.is-link a{margin-left:0!important;margin-top:0!important;width:auto!important}@keyframes jetpack-memberships\_button\_\_spinner-animation{to{transform:rotate(1turn)}}.jetpack-memberships-spinner{display:none;height:1em;margin:0 0 0 5px;width:1em}.jetpack-memberships-spinner svg{height:100%;margin-bottom:-2px;width:100%}.jetpack-memberships-spinner-rotating{animation:jetpack-memberships\_button\_\_spinner-animation .75s linear infinite;transform-origin:center}.is-loading .jetpack-memberships-spinner{display:inline-block}body.jetpack-memberships-modal-open{overflow:hidden}dialog.jetpack-memberships-modal{opacity:1}dialog.jetpack-memberships-modal,dialog.jetpack-memberships-modal iframe{background:#0000;border:0;bottom:0;box-shadow:none;height:100%;left:0;margin:0;padding:0;position:fixed;right:0;top:0;width:100%}dialog.jetpack-memberships-modal::backdrop{background-color:#000;opacity:.7;transition:opacity .2s ease-out}dialog.jetpack-memberships-modal.is-loading,dialog.jetpack-memberships-modal.is-loading::backdrop{opacity:0}
/\*# sourceURL=/wp-content/mu-plugins/jetpack-plugin/moon/\_inc/blocks/subscriptions/view.css?minify=false \*/


.wp-block-group{box-sizing:border-box}:where(.wp-block-group.wp-block-group-is-layout-constrained){position:relative}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/group/style.min.css \*/

.wp-block-post-title{box-sizing:border-box;word-break:break-word}.wp-block-post-title :where(a){display:inline-block;font-family:inherit;font-size:inherit;font-style:inherit;font-weight:inherit;letter-spacing:inherit;line-height:inherit;text-decoration:inherit}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/post-title/style.min.css \*/

.is-small-text{font-size:.875em}.is-regular-text{font-size:1em}.is-large-text{font-size:2.25em}.is-larger-text{font-size:3em}.has-drop-cap:not(:focus):first-letter{float:left;font-size:8.4em;font-style:normal;font-weight:100;line-height:.68;margin:.05em .1em 0 0;text-transform:uppercase}body.rtl .has-drop-cap:not(:focus):first-letter{float:none;margin-left:.1em}p.has-drop-cap.has-background{overflow:hidden}:root :where(p.has-background){padding:1.25em 2.375em}:where(p.has-text-color:not(.has-link-color)) a{color:inherit}p.has-text-align-left[style\*="writing-mode:vertical-lr"],p.has-text-align-right[style\*="writing-mode:vertical-rl"]{rotate:180deg}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/paragraph/style.min.css \*/

.wp-block-post-author-name{box-sizing:border-box}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/post-author-name/style.min.css \*/

.wp-block-post-terms{box-sizing:border-box}.wp-block-post-terms .wp-block-post-terms\_\_separator{white-space:pre-wrap}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/post-terms/style.min.css \*/

h1:where(.wp-block-heading).has-background,h2:where(.wp-block-heading).has-background,h3:where(.wp-block-heading).has-background,h4:where(.wp-block-heading).has-background,h5:where(.wp-block-heading).has-background,h6:where(.wp-block-heading).has-background{padding:1.25em 2.375em}h1.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h1.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h2.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h2.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h3.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h3.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h4.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h4.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h5.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h5.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h6.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h6.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]){rotate:180deg}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/heading/style.min.css \*/

.wp-block-post-content{display:flow-root}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/post-content/style.min.css \*/

@charset "UTF-8";.wp-block-separator{border:none;border-top:2px solid}:root :where(.wp-block-separator.is-style-dots){height:auto;line-height:1;text-align:center}:root :where(.wp-block-separator.is-style-dots):before{color:currentColor;content:"···";font-family:serif;font-size:1.5em;letter-spacing:2em;padding-left:2em}.wp-block-separator.is-style-dots{background:none!important;border:none!important}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/separator/style.min.css \*/

.wp-block-post-navigation-link .wp-block-post-navigation-link\_\_arrow-previous{display:inline-block;margin-right:1ch}.wp-block-post-navigation-link .wp-block-post-navigation-link\_\_arrow-previous:not(.is-arrow-chevron){transform:scaleX(1)}.wp-block-post-navigation-link .wp-block-post-navigation-link\_\_arrow-next{display:inline-block;margin-left:1ch}.wp-block-post-navigation-link .wp-block-post-navigation-link\_\_arrow-next:not(.is-arrow-chevron){transform:scaleX(1)}.wp-block-post-navigation-link.has-text-align-left[style\*="writing-mode: vertical-lr"],.wp-block-post-navigation-link.has-text-align-right[style\*="writing-mode: vertical-rl"]{rotate:180deg}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/post-navigation-link/style.min.css \*/

.wp-block-avatar{line-height:0}.wp-block-avatar,.wp-block-avatar img{box-sizing:border-box}.wp-block-avatar.aligncenter{text-align:center}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/avatar/style.min.css \*/

.wp-block-comment-date{box-sizing:border-box}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/comment-date/style.min.css \*/

.wp-block-comment-author-name{box-sizing:border-box}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/comment-author-name/style.min.css \*/

.comment-awaiting-moderation{display:block;font-size:.875em;line-height:1.5}.wp-block-comment-content{box-sizing:border-box}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/comment-content/style.min.css \*/

.wp-block-comment-template{box-sizing:border-box;list-style:none;margin-bottom:0;max-width:100%;padding:0}.wp-block-comment-template li{clear:both}.wp-block-comment-template ol{list-style:none;margin-bottom:0;max-width:100%;padding-left:2rem}.wp-block-comment-template.alignleft{float:left}.wp-block-comment-template.aligncenter{margin-left:auto;margin-right:auto;width:fit-content}.wp-block-comment-template.alignright{float:right}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/comment-template/style.min.css \*/

.wp-block-post-comments{box-sizing:border-box}.wp-block-post-comments .alignleft{float:left}.wp-block-post-comments .alignright{float:right}.wp-block-post-comments .navigation:after{clear:both;content:"";display:table}.wp-block-post-comments .commentlist{clear:both;list-style:none;margin:0;padding:0}.wp-block-post-comments .commentlist .comment{min-height:2.25em;padding-left:3.25em}.wp-block-post-comments .commentlist .comment p{font-size:1em;line-height:1.8;margin:1em 0}.wp-block-post-comments .commentlist .children{list-style:none;margin:0;padding:0}.wp-block-post-comments .comment-author{line-height:1.5}.wp-block-post-comments .comment-author .avatar{border-radius:1.5em;display:block;float:left;height:2.5em;margin-right:.75em;margin-top:.5em;width:2.5em}.wp-block-post-comments .comment-author cite{font-style:normal}.wp-block-post-comments .comment-meta{font-size:.875em;line-height:1.5}.wp-block-post-comments .comment-meta b{font-weight:400}.wp-block-post-comments .comment-meta .comment-awaiting-moderation{display:block;margin-bottom:1em;margin-top:1em}.wp-block-post-comments .comment-body .commentmetadata{font-size:.875em}.wp-block-post-comments .comment-form-author label,.wp-block-post-comments .comment-form-comment label,.wp-block-post-comments .comment-form-email label,.wp-block-post-comments .comment-form-url label{display:block;margin-bottom:.25em}.wp-block-post-comments .comment-form input:not([type=submit]):not([type=checkbox]),.wp-block-post-comments .comment-form textarea{box-sizing:border-box;display:block;width:100%}.wp-block-post-comments .comment-form-cookies-consent{display:flex;gap:.25em}.wp-block-post-comments .comment-form-cookies-consent #wp-comment-cookies-consent{margin-top:.35em}.wp-block-post-comments .comment-reply-title{margin-bottom:0}.wp-block-post-comments .comment-reply-title :where(small){font-size:var(--wp--preset--font-size--medium,smaller);margin-left:.5em}.wp-block-post-comments .reply{font-size:.875em;margin-bottom:1.4em}.wp-block-post-comments input:not([type=submit]),.wp-block-post-comments textarea{border:1px solid #949494;font-family:inherit;font-size:1em}.wp-block-post-comments input:not([type=submit]):not([type=checkbox]),.wp-block-post-comments textarea{padding:calc(.667em + 2px)}:where(.wp-block-post-comments input[type=submit]){border:none}.wp-block-comments{box-sizing:border-box}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/comments/style.min.css \*/

.wp-block-post-date{box-sizing:border-box}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/post-date/style.min.css \*/

.wp-block-post-template{box-sizing:border-box;list-style:none;margin-bottom:0;margin-top:0;max-width:100%;padding:0}.wp-block-post-template.is-flex-container{display:flex;flex-direction:row;flex-wrap:wrap;gap:1.25em}.wp-block-post-template.is-flex-container>li{margin:0;width:100%}@media (min-width:600px){.wp-block-post-template.is-flex-container.is-flex-container.columns-2>li{width:calc(50% - .625em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-3>li{width:calc(33.33333% - .83333em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-4>li{width:calc(25% - .9375em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-5>li{width:calc(20% - 1em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-6>li{width:calc(16.66667% - 1.04167em)}}@media (max-width:600px){.wp-block-post-template-is-layout-grid.wp-block-post-template-is-layout-grid.wp-block-post-template-is-layout-grid.wp-block-post-template-is-layout-grid{grid-template-columns:1fr}}.wp-block-post-template-is-layout-constrained>li>.alignright,.wp-block-post-template-is-layout-flow>li>.alignright{float:right;margin-inline-end:0;margin-inline-start:2em}.wp-block-post-template-is-layout-constrained>li>.alignleft,.wp-block-post-template-is-layout-flow>li>.alignleft{float:left;margin-inline-end:2em;margin-inline-start:0}.wp-block-post-template-is-layout-constrained>li>.aligncenter,.wp-block-post-template-is-layout-flow>li>.aligncenter{margin-inline-end:auto;margin-inline-start:auto}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/post-template/style.min.css \*/

.wp-block-site-tagline{box-sizing:border-box}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/site-tagline/style.min.css \*/

.wp-block-spacer{clear:both}
/\*# sourceURL=https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/styles/block-library/spacer/style.min.css \*/

:root{--wp-block-synced-color:#7a00df;--wp-block-synced-color--rgb:122,0,223;--wp-bound-block-color:var(--wp-block-synced-color);--wp-editor-canvas-background:#ddd;--wp-admin-theme-color:#007cba;--wp-admin-theme-color--rgb:0,124,186;--wp-admin-theme-color-darker-10:#006ba1;--wp-admin-theme-color-darker-10--rgb:0,107,160.5;--wp-admin-theme-color-darker-20:#005a87;--wp-admin-theme-color-darker-20--rgb:0,90,135;--wp-admin-border-width-focus:2px}@media (min-resolution:192dpi){:root{--wp-admin-border-width-focus:1.5px}}.wp-element-button{cursor:pointer}:root .has-very-light-gray-background-color{background-color:#eee}:root .has-very-dark-gray-background-color{background-color:#313131}:root .has-very-light-gray-color{color:#eee}:root .has-very-dark-gray-color{color:#313131}:root .has-vivid-green-cyan-to-vivid-cyan-blue-gradient-background{background:linear-gradient(135deg,#00d084,#0693e3)}:root .has-purple-crush-gradient-background{background:linear-gradient(135deg,#34e2e4,#4721fb 50%,#ab1dfe)}:root .has-hazy-dawn-gradient-background{background:linear-gradient(135deg,#faaca8,#dad0ec)}:root .has-subdued-olive-gradient-background{background:linear-gradient(135deg,#fafae1,#67a671)}:root .has-atomic-cream-gradient-background{background:linear-gradient(135deg,#fdd79a,#004a59)}:root .has-nightshade-gradient-background{background:linear-gradient(135deg,#330968,#31cdcf)}:root .has-midnight-gradient-background{background:linear-gradient(135deg,#020381,#2874fc)}:root{--wp--preset--font-size--normal:16px;--wp--preset--font-size--huge:42px}.has-regular-font-size{font-size:1em}.has-larger-font-size{font-size:2.625em}.has-normal-font-size{font-size:var(--wp--preset--font-size--normal)}.has-huge-font-size{font-size:var(--wp--preset--font-size--huge)}:root .has-text-align-center{text-align:center}:root .has-text-align-left{text-align:left}:root .has-text-align-right{text-align:right}.has-fit-text{white-space:nowrap!important}#end-resizable-editor-section{display:none}.aligncenter{clear:both}.items-justified-left{justify-content:flex-start}.items-justified-center{justify-content:center}.items-justified-right{justify-content:flex-end}.items-justified-space-between{justify-content:space-between}.screen-reader-text{word-wrap:normal!important;border:0;clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px;word-break:normal!important}.screen-reader-text:focus{background-color:#ddd;clip-path:none;color:#444;display:block;font-size:1em;height:auto;left:5px;line-height:normal;padding:15px 23px 14px;text-decoration:none;top:5px;width:auto;z-index:100000}html :where(.has-border-color){border-style:solid}html :where([style\*=border-color]){border-style:solid}html :where([style\*=border-top-color]){border-top-style:solid}html :where([style\*=border-right-color]){border-right-style:solid}html :where([style\*=border-bottom-color]){border-bottom-style:solid}html :where([style\*=border-left-color]){border-left-style:solid}html :where([style\*=border-width]){border-style:solid}html :where([style\*=border-top-width]){border-top-style:solid}html :where([style\*=border-right-width]){border-right-style:solid}html :where([style\*=border-bottom-width]){border-bottom-style:solid}html :where([style\*=border-left-width]){border-left-style:solid}html :where(img[class\*=wp-image-]){height:auto;max-width:100%}:where(figure){margin:0 0 1em}html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:var(--wp-admin--admin-bar--height,0px)}@media screen and (max-width:600px){html :where(.is-position-sticky){--wp-admin--admin-bar--position-offset:0px}}
.has-text-align-justify {
text-align:justify;
}
.has-text-align-justify{text-align:justify;}
/\*# sourceURL=wp-block-library-inline-css \*/

:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--color--base: #FFFFFF;--wp--preset--color--contrast: #111111;--wp--preset--color--accent-1: #FFEE58;--wp--preset--color--accent-2: #F6CFF4;--wp--preset--color--accent-3: #503AA8;--wp--preset--color--accent-4: #686868;--wp--preset--color--accent-5: #FBFAF3;--wp--preset--color--accent-6: color-mix(in srgb, currentColor 20%, transparent);--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgb(6,147,227) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgb(252,185,0) 0%,rgb(255,105,0) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgb(255,105,0) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 0.875rem;--wp--preset--font-size--medium: clamp(1rem, 1rem + ((1vw - 0.2rem) \* 0.196), 1.125rem);--wp--preset--font-size--large: clamp(1.125rem, 1.125rem + ((1vw - 0.2rem) \* 0.392), 1.375rem);--wp--preset--font-size--x-large: clamp(1.75rem, 1.75rem + ((1vw - 0.2rem) \* 0.392), 2rem);--wp--preset--font-size--xx-large: clamp(2.15rem, 2.15rem + ((1vw - 0.2rem) \* 1.333), 3rem);--wp--preset--font-family--albert-sans: 'Albert Sans', sans-serif;--wp--preset--font-family--alegreya: Alegreya, serif;--wp--preset--font-family--arvo: Arvo, serif;--wp--preset--font-family--bodoni-moda: 'Bodoni Moda', serif;--wp--preset--font-family--bricolage-grotesque: 'Bricolage Grotesque', sans-serif;--wp--preset--font-family--cabin: Cabin, sans-serif;--wp--preset--font-family--chivo: Chivo, sans-serif;--wp--preset--font-family--commissioner: Commissioner, sans-serif;--wp--preset--font-family--cormorant: Cormorant, serif;--wp--preset--font-family--courier-prime: 'Courier Prime', monospace;--wp--preset--font-family--crimson-pro: 'Crimson Pro', serif;--wp--preset--font-family--dm-mono: 'DM Mono', monospace;--wp--preset--font-family--dm-sans: 'DM Sans', sans-serif;--wp--preset--font-family--dm-serif-display: 'DM Serif Display', serif;--wp--preset--font-family--domine: Domine, serif;--wp--preset--font-family--eb-garamond: 'EB Garamond', serif;--wp--preset--font-family--epilogue: Epilogue, sans-serif;--wp--preset--font-family--fahkwang: Fahkwang, sans-serif;--wp--preset--font-family--figtree: Figtree, sans-serif;--wp--preset--font-family--fira-sans: 'Fira Sans', sans-serif;--wp--preset--font-family--fjalla-one: 'Fjalla One', sans-serif;--wp--preset--font-family--fraunces: Fraunces, serif;--wp--preset--font-family--gabarito: Gabarito, system-ui;--wp--preset--font-family--ibm-plex-mono: 'IBM Plex Mono', monospace;--wp--preset--font-family--ibm-plex-sans: 'IBM Plex Sans', sans-serif;--wp--preset--font-family--ibarra-real-nova: 'Ibarra Real Nova', serif;--wp--preset--font-family--instrument-serif: 'Instrument Serif', serif;--wp--preset--font-family--inter: Inter, sans-serif;--wp--preset--font-family--josefin-sans: 'Josefin Sans', sans-serif;--wp--preset--font-family--jost: Jost, sans-serif;--wp--preset--font-family--libre-baskerville: 'Libre Baskerville', serif;--wp--preset--font-family--libre-franklin: 'Libre Franklin', sans-serif;--wp--preset--font-family--literata: Literata, serif;--wp--preset--font-family--lora: Lora, serif;--wp--preset--font-family--merriweather: Merriweather, serif;--wp--preset--font-family--montserrat: Montserrat, sans-serif;--wp--preset--font-family--newsreader: Newsreader, serif;--wp--preset--font-family--noto-sans-mono: 'Noto Sans Mono', sans-serif;--wp--preset--font-family--nunito: Nunito, sans-serif;--wp--preset--font-family--open-sans: 'Open Sans', sans-serif;--wp--preset--font-family--overpass: Overpass, sans-serif;--wp--preset--font-family--pt-serif: 'PT Serif', serif;--wp--preset--font-family--petrona: Petrona, serif;--wp--preset--font-family--piazzolla: Piazzolla, serif;--wp--preset--font-family--playfair-display: 'Playfair Display', serif;--wp--preset--font-family--plus-jakarta-sans: 'Plus Jakarta Sans', sans-serif;--wp--preset--font-family--poppins: Poppins, sans-serif;--wp--preset--font-family--raleway: Raleway, sans-serif;--wp--preset--font-family--roboto: Roboto, sans-serif;--wp--preset--font-family--roboto-slab: 'Roboto Slab', serif;--wp--preset--font-family--rubik: Rubik, sans-serif;--wp--preset--font-family--rufina: Rufina, serif;--wp--preset--font-family--sora: Sora, sans-serif;--wp--preset--font-family--source-sans-3: 'Source Sans 3', sans-serif;--wp--preset--font-family--source-serif-4: 'Source Serif 4', serif;--wp--preset--font-family--space-mono: 'Space Mono', monospace;--wp--preset--font-family--syne: Syne, sans-serif;--wp--preset--font-family--texturina: Texturina, serif;--wp--preset--font-family--urbanist: Urbanist, sans-serif;--wp--preset--font-family--work-sans: 'Work Sans', sans-serif;--wp--preset--font-family--manrope: Manrope, sans-serif;--wp--preset--font-family--fira-code: "Fira Code", monospace;--wp--preset--spacing--20: 10px;--wp--preset--spacing--30: 20px;--wp--preset--spacing--40: 30px;--wp--preset--spacing--50: clamp(30px, 5vw, 50px);--wp--preset--spacing--60: clamp(30px, 7vw, 70px);--wp--preset--spacing--70: clamp(50px, 7vw, 90px);--wp--preset--spacing--80: clamp(70px, 10vw, 140px);--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgb(255, 255, 255), 6px 6px rgb(0, 0, 0);--wp--preset--shadow--crisp: 6px 6px 0px rgb(0, 0, 0);}.wp-block-button{--wp--preset--dimension--25: 25%;--wp--preset--dimension--50: 50%;--wp--preset--dimension--75: 75%;--wp--preset--dimension--100: 100%;}:root { --wp--style--global--content-size: 645px;--wp--style--global--wide-size: 1340px; }:where(body) { margin: 0; }.wp-site-blocks { padding-top: var(--wp--style--root--padding-top); padding-bottom: var(--wp--style--root--padding-bottom); }.has-global-padding { padding-right: var(--wp--style--root--padding-right); padding-left: var(--wp--style--root--padding-left); }.has-global-padding > .alignfull { margin-right: calc(var(--wp--style--root--padding-right) \* -1); margin-left: calc(var(--wp--style--root--padding-left) \* -1); }.has-global-padding :where(:not(.alignfull.is-layout-flow) > .has-global-padding:not(.wp-block-block, .alignfull)) { padding-right: 0; padding-left: 0; }.has-global-padding :where(:not(.alignfull.is-layout-flow) > .has-global-padding:not(.wp-block-block, .alignfull)) > .alignfull { margin-left: 0; margin-right: 0; }.wp-site-blocks > .alignleft { float: left; margin-right: 2em; }.wp-site-blocks > .alignright { float: right; margin-left: 2em; }.wp-site-blocks > .aligncenter { justify-content: center; margin-left: auto; margin-right: auto; }:where(.wp-site-blocks) > \* { margin-block-start: 1.2rem; margin-block-end: 0; }:where(.wp-site-blocks) > :first-child { margin-block-start: 0; }:where(.wp-site-blocks) > :last-child { margin-block-end: 0; }:root { --wp--style--block-gap: 1.2rem; }:root :where(.is-layout-flow) > :first-child{margin-block-start: 0;}:root :where(.is-layout-flow) > :last-child{margin-block-end: 0;}:root :where(.is-layout-flow) > \*{margin-block-start: 1.2rem;margin-block-end: 0;}:root :where(.is-layout-constrained) > :first-child{margin-block-start: 0;}:root :where(.is-layout-constrained) > :last-child{margin-block-end: 0;}:root :where(.is-layout-constrained) > \*{margin-block-start: 1.2rem;margin-block-end: 0;}:root :where(.is-layout-flex){gap: 1.2rem;}:root :where(.is-layout-grid){gap: 1.2rem;}.is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width: var(--wp--style--global--content-size);margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignwide{max-width: var(--wp--style--global--wide-size);}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(\*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(\*, div){margin: 0;}body{background-color: var(--wp--preset--color--base);color: var(--wp--preset--color--contrast);font-family: var(--wp--preset--font-family--manrope);font-size: var(--wp--preset--font-size--large);font-weight: 300;letter-spacing: -0.1px;line-height: 1.4;--wp--style--root--padding-top: 0px;--wp--style--root--padding-right: var(--wp--preset--spacing--50);--wp--style--root--padding-bottom: 0px;--wp--style--root--padding-left: var(--wp--preset--spacing--50);}a:where(:not(.wp-element-button)){color: currentColor;}:root :where(a:where(:not(.wp-element-button)):hover){text-decoration: none;}h1, h2, h3, h4, h5, h6{font-weight: 400;letter-spacing: -0.1px;line-height: 1.125;}h1{font-size: var(--wp--preset--font-size--xx-large);}h2{font-size: var(--wp--preset--font-size--x-large);}h3{font-size: var(--wp--preset--font-size--large);}h4{font-size: var(--wp--preset--font-size--medium);}h5{font-size: var(--wp--preset--font-size--small);letter-spacing: 0.5px;}h6{font-size: var(--wp--preset--font-size--small);font-weight: 700;letter-spacing: 1.4px;text-transform: uppercase;}:root :where(.wp-element-button, .wp-block-button\_\_link){background-color: var(--wp--preset--color--contrast);border-width: 0;color: var(--wp--preset--color--base);font-family: inherit;font-size: var(--wp--preset--font-size--medium);font-style: inherit;font-weight: inherit;letter-spacing: inherit;line-height: inherit;padding-top: 1rem;padding-right: 2.25rem;padding-bottom: 1rem;padding-left: 2.25rem;text-decoration: none;text-transform: inherit;}:root :where(.wp-element-button:hover, .wp-block-button\_\_link:hover){background-color: color-mix(in srgb, var(--wp--preset--color--contrast) 85%, transparent);border-color: transparent;color: var(--wp--preset--color--base);}:root :where(.wp-element-button:focus, .wp-block-button\_\_link:focus){outline-color: var(--wp--preset--color--accent-4);outline-offset: 2px;}:root :where(.wp-element-caption, .wp-block-audio figcaption, .wp-block-embed figcaption, .wp-block-gallery figcaption, .wp-block-image figcaption, .wp-block-table figcaption, .wp-block-video figcaption){font-size: var(--wp--preset--font-size--small);line-height: 1.4;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-base-color{color: var(--wp--preset--color--base) !important;}.has-contrast-color{color: var(--wp--preset--color--contrast) !important;}.has-accent-1-color{color: var(--wp--preset--color--accent-1) !important;}.has-accent-2-color{color: var(--wp--preset--color--accent-2) !important;}.has-accent-3-color{color: var(--wp--preset--color--accent-3) !important;}.has-accent-4-color{color: var(--wp--preset--color--accent-4) !important;}.has-accent-5-color{color: var(--wp--preset--color--accent-5) !important;}.has-accent-6-color{color: var(--wp--preset--color--accent-6) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-base-background-color{background-color: var(--wp--preset--color--base) !important;}.has-contrast-background-color{background-color: var(--wp--preset--color--contrast) !important;}.has-accent-1-background-color{background-color: var(--wp--preset--color--accent-1) !important;}.has-accent-2-background-color{background-color: var(--wp--preset--color--accent-2) !important;}.has-accent-3-background-color{background-color: var(--wp--preset--color--accent-3) !important;}.has-accent-4-background-color{background-color: var(--wp--preset--color--accent-4) !important;}.has-accent-5-background-color{background-color: var(--wp--preset--color--accent-5) !important;}.has-accent-6-background-color{background-color: var(--wp--preset--color--accent-6) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-base-border-color{border-color: var(--wp--preset--color--base) !important;}.has-contrast-border-color{border-color: var(--wp--preset--color--contrast) !important;}.has-accent-1-border-color{border-color: var(--wp--preset--color--accent-1) !important;}.has-accent-2-border-color{border-color: var(--wp--preset--color--accent-2) !important;}.has-accent-3-border-color{border-color: var(--wp--preset--color--accent-3) !important;}.has-accent-4-border-color{border-color: var(--wp--preset--color--accent-4) !important;}.has-accent-5-border-color{border-color: var(--wp--preset--color--accent-5) !important;}.has-accent-6-border-color{border-color: var(--wp--preset--color--accent-6) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}.has-xx-large-font-size{font-size: var(--wp--preset--font-size--xx-large) !important;}.has-albert-sans-font-family{font-family: var(--wp--preset--font-family--albert-sans) !important;}.has-alegreya-font-family{font-family: var(--wp--preset--font-family--alegreya) !important;}.has-arvo-font-family{font-family: var(--wp--preset--font-family--arvo) !important;}.has-bodoni-moda-font-family{font-family: var(--wp--preset--font-family--bodoni-moda) !important;}.has-bricolage-grotesque-font-family{font-family: var(--wp--preset--font-family--bricolage-grotesque) !important;}.has-cabin-font-family{font-family: var(--wp--preset--font-family--cabin) !important;}.has-chivo-font-family{font-family: var(--wp--preset--font-family--chivo) !important;}.has-commissioner-font-family{font-family: var(--wp--preset--font-family--commissioner) !important;}.has-cormorant-font-family{font-family: var(--wp--preset--font-family--cormorant) !important;}.has-courier-prime-font-family{font-family: var(--wp--preset--font-family--courier-prime) !important;}.has-crimson-pro-font-family{font-family: var(--wp--preset--font-family--crimson-pro) !important;}.has-dm-mono-font-family{font-family: var(--wp--preset--font-family--dm-mono) !important;}.has-dm-sans-font-family{font-family: var(--wp--preset--font-family--dm-sans) !important;}.has-dm-serif-display-font-family{font-family: var(--wp--preset--font-family--dm-serif-display) !important;}.has-domine-font-family{font-family: var(--wp--preset--font-family--domine) !important;}.has-eb-garamond-font-family{font-family: var(--wp--preset--font-family--eb-garamond) !important;}.has-epilogue-font-family{font-family: var(--wp--preset--font-family--epilogue) !important;}.has-fahkwang-font-family{font-family: var(--wp--preset--font-family--fahkwang) !important;}.has-figtree-font-family{font-family: var(--wp--preset--font-family--figtree) !important;}.has-fira-sans-font-family{font-family: var(--wp--preset--font-family--fira-sans) !important;}.has-fjalla-one-font-family{font-family: var(--wp--preset--font-family--fjalla-one) !important;}.has-fraunces-font-family{font-family: var(--wp--preset--font-family--fraunces) !important;}.has-gabarito-font-family{font-family: var(--wp--preset--font-family--gabarito) !important;}.has-ibm-plex-mono-font-family{font-family: var(--wp--preset--font-family--ibm-plex-mono) !important;}.has-ibm-plex-sans-font-family{font-family: var(--wp--preset--font-family--ibm-plex-sans) !important;}.has-ibarra-real-nova-font-family{font-family: var(--wp--preset--font-family--ibarra-real-nova) !important;}.has-instrument-serif-font-family{font-family: var(--wp--preset--font-family--instrument-serif) !important;}.has-inter-font-family{font-family: var(--wp--preset--font-family--inter) !important;}.has-josefin-sans-font-family{font-family: var(--wp--preset--font-family--josefin-sans) !important;}.has-jost-font-family{font-family: var(--wp--preset--font-family--jost) !important;}.has-libre-baskerville-font-family{font-family: var(--wp--preset--font-family--libre-baskerville) !important;}.has-libre-franklin-font-family{font-family: var(--wp--preset--font-family--libre-franklin) !important;}.has-literata-font-family{font-family: var(--wp--preset--font-family--literata) !important;}.has-lora-font-family{font-family: var(--wp--preset--font-family--lora) !important;}.has-merriweather-font-family{font-family: var(--wp--preset--font-family--merriweather) !important;}.has-montserrat-font-family{font-family: var(--wp--preset--font-family--montserrat) !important;}.has-newsreader-font-family{font-family: var(--wp--preset--font-family--newsreader) !important;}.has-noto-sans-mono-font-family{font-family: var(--wp--preset--font-family--noto-sans-mono) !important;}.has-nunito-font-family{font-family: var(--wp--preset--font-family--nunito) !important;}.has-open-sans-font-family{font-family: var(--wp--preset--font-family--open-sans) !important;}.has-overpass-font-family{font-family: var(--wp--preset--font-family--overpass) !important;}.has-pt-serif-font-family{font-family: var(--wp--preset--font-family--pt-serif) !important;}.has-petrona-font-family{font-family: var(--wp--preset--font-family--petrona) !important;}.has-piazzolla-font-family{font-family: var(--wp--preset--font-family--piazzolla) !important;}.has-playfair-display-font-family{font-family: var(--wp--preset--font-family--playfair-display) !important;}.has-plus-jakarta-sans-font-family{font-family: var(--wp--preset--font-family--plus-jakarta-sans) !important;}.has-poppins-font-family{font-family: var(--wp--preset--font-family--poppins) !important;}.has-raleway-font-family{font-family: var(--wp--preset--font-family--raleway) !important;}.has-roboto-font-family{font-family: var(--wp--preset--font-family--roboto) !important;}.has-roboto-slab-font-family{font-family: var(--wp--preset--font-family--roboto-slab) !important;}.has-rubik-font-family{font-family: var(--wp--preset--font-family--rubik) !important;}.has-rufina-font-family{font-family: var(--wp--preset--font-family--rufina) !important;}.has-sora-font-family{font-family: var(--wp--preset--font-family--sora) !important;}.has-source-sans-3-font-family{font-family: var(--wp--preset--font-family--source-sans-3) !important;}.has-source-serif-4-font-family{font-family: var(--wp--preset--font-family--source-serif-4) !important;}.has-space-mono-font-family{font-family: var(--wp--preset--font-family--space-mono) !important;}.has-syne-font-family{font-family: var(--wp--preset--font-family--syne) !important;}.has-texturina-font-family{font-family: var(--wp--preset--font-family--texturina) !important;}.has-urbanist-font-family{font-family: var(--wp--preset--font-family--urbanist) !important;}.has-work-sans-font-family{font-family: var(--wp--preset--font-family--work-sans) !important;}.has-manrope-font-family{font-family: var(--wp--preset--font-family--manrope) !important;}.has-fira-code-font-family{font-family: var(--wp--preset--font-family--fira-code) !important;}
:root :where(.wp-block-avatar img){border-radius: 100px;}
:root :where(.wp-block-comment-author-name){color: var(--wp--preset--color--accent-4);font-size: var(--wp--preset--font-size--small);margin-top: 5px;margin-bottom: 0px;}
:root :where(.wp-block-comment-author-name a:where(:not(.wp-element-button))){color: var(--wp--preset--color--accent-4);text-decoration: none;}
:root :where(.wp-block-comment-author-name a:where(:not(.wp-element-button)):hover){text-decoration: underline;}
:root :where(.wp-block-comment-content){font-size: var(--wp--preset--font-size--medium);margin-top: var(--wp--preset--spacing--30);margin-bottom: var(--wp--preset--spacing--30);}
:root :where(.wp-block-comment-date){color: var(--wp--preset--color--contrast);font-size: var(--wp--preset--font-size--small);}
:root :where(.wp-block-comment-date a:where(:not(.wp-element-button))){color: var(--wp--preset--color--contrast);}
:root :where(.wp-block-post-date){color: var(--wp--preset--color--accent-4);font-size: var(--wp--preset--font-size--small);}
:root :where(.wp-block-post-date a:where(:not(.wp-element-button))){color: var(--wp--preset--color--accent-4);text-decoration: none;}
:root :where(.wp-block-post-date a:where(:not(.wp-element-button)):hover){text-decoration: underline;}
:root :where(.wp-block-post-navigation-link){font-size: var(--wp--preset--font-size--medium);}
:root :where(.wp-block-post-terms){font-size: var(--wp--preset--font-size--small);font-weight: 600;}:root :where(.wp-block-post-terms a){white-space: nowrap;}
:root :where(.wp-block-post-title a:where(:not(.wp-element-button))){text-decoration: none;}
:root :where(.wp-block-post-title a:where(:not(.wp-element-button)):hover){text-decoration: underline;}
:root :where(.wp-block-separator){border-color: currentColor;border-width: 0 0 1px 0;border-style: solid;color: var(--wp--preset--color--accent-6);}
:root :where(.wp-block-site-tagline){font-size: var(--wp--preset--font-size--medium);}
:root :where(.wp-block-site-title){font-weight: 700;letter-spacing: -.5px;}
:root :where(.wp-block-site-title a:where(:not(.wp-element-button))){text-decoration: none;}
:root :where(.wp-block-site-title a:where(:not(.wp-element-button)):hover){text-decoration: underline;}
:root :where(.wp-block-navigation){font-size: var(--wp--preset--font-size--medium);}
:root :where(.wp-block-navigation a:where(:not(.wp-element-button))){text-decoration: none;}
:root :where(.wp-block-navigation a:where(:not(.wp-element-button)):hover){text-decoration: underline;}
/\*# sourceURL=global-styles-inline-css \*/

:root :where(.wp-block-separator.is-style-wide--2){}:root :where(.wp-block-separator.is-style-wide--2:not(.alignfull)){max-width: var(--wp--style--global--wide-size) !important;}
:root :where(.is-style-post-terms-1--3 a:where(:not(.wp-element-button))){border-radius: 20px;border-color: var(--wp--preset--color--accent-6);border-width: 0.8px;border-style: solid;font-weight: 400;line-height: 2.8;padding-top: 5px;padding-right: 10px;padding-bottom: 5px;padding-left: 10px;text-decoration: none;}:root :where(.is-style-post-terms-1--3 a:where(:not(.wp-element-button)):hover){text-decoration: underline;}
/\*# sourceURL=block-style-variation-styles-inline-css \*/

img.wp-smiley, img.emoji {
display: inline !important;
border: none !important;
box-shadow: none !important;
height: 1em !important;
width: 1em !important;
margin: 0 0.07em !important;
vertical-align: -0.1em !important;
background: none !important;
padding: 0 !important;
}
/\*# sourceURL=wp-emoji-styles-inline-css \*/


/\*! This file is auto-generated \*/
.skip-link.screen-reader-text{border:0;clip-path:inset(50%);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute!important;width:1px;word-wrap:normal!important;word-break:normal!important}.skip-link.screen-reader-text:focus{background-color:#eee;clip-path:none;color:#444;display:block;font-size:1em;height:auto;left:5px;line-height:normal;padding:15px 23px 14px;text-decoration:none;top:5px;width:auto;z-index:100000}
/\*# sourceURL=/wp-includes/css/wp-block-template-skip-link.min.css \*/


.wp-container-core-navigation-is-layout-6e943505{justify-content:flex-end;}.wp-container-core-group-is-layout-fbffc046{flex-wrap:nowrap;gap:var(--wp--preset--spacing--10);justify-content:flex-end;}.wp-container-core-group-is-layout-ec1e7a1e{flex-wrap:nowrap;justify-content:space-between;}.wp-container-core-group-is-layout-fd1a9a6d{gap:0.2em;}.wp-container-core-group-is-layout-f2b6297b > :where(:not(.alignleft):not(.alignright):not(.alignfull)){max-width:480px;margin-left:auto !important;margin-right:auto !important;}.wp-container-core-group-is-layout-f2b6297b > .alignwide{max-width:480px;}.wp-container-core-group-is-layout-f2b6297b .alignfull{max-width:none;}.wp-container-core-group-is-layout-878fe601{flex-wrap:nowrap;justify-content:space-between;}.wp-container-core-group-is-layout-3a88641f{flex-wrap:nowrap;}.wp-container-core-group-is-layout-40af6500{flex-wrap:nowrap;align-items:flex-start;}.wp-container-core-group-is-layout-cba70755{flex-wrap:nowrap;justify-content:space-between;align-items:center;}.wp-container-core-post-template-is-layout-b4d04ffe > \*{margin-block-start:0;margin-block-end:0;}.wp-container-core-post-template-is-layout-b4d04ffe > \* + \*{margin-block-start:0;margin-block-end:0;}.wp-container-core-group-is-layout-5ef3efcf{gap:var(--wp--preset--spacing--10);flex-direction:column;align-items:center;}
/\*# sourceURL=core-block-supports-inline-css \*/


a{text-decoration-thickness:1px!important;text-underline-offset:.1em}:where(.wp-site-blocks :focus){outline-style:solid;outline-width:2px}.wp-block-navigation .wp-block-navigation-submenu .wp-block-navigation-item:not(:last-child){margin-bottom:3px}.wp-block-navigation .wp-block-navigation-item .wp-block-navigation-item\_\_content{outline-offset:4px}.wp-block-navigation .wp-block-navigation-item ul.wp-block-navigation\_\_submenu-container .wp-block-navigation-item\_\_content{outline-offset:0}blockquote,caption,figcaption,h1,h2,h3,h4,h5,h6,p{text-wrap:pretty}.more-link{display:block}:where(pre){overflow-x:auto}
/\*# sourceURL=https://s0.wp.com/wp-content/themes/pub/twentytwentyfive/style.min.css \*/


:root { --font-headings: unset; --font-base: unset; --font-headings-default: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif; --font-base-default: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;}
/\*# sourceURL=jetpack-global-styles-frontend-style-inline-css \*/


var Jetpack\_Block\_Assets\_Base\_Url="https://s0.wp.com/wp-content/mu-plugins/jetpack-plugin/moon/\_inc/blocks/";
//# sourceURL=jetpack-blocks-assets-base-url-js-before

var JETPACK\_MU\_WPCOM\_SETTINGS = {"assetsUrl":"https://s0.wp.com/wp-content/mu-plugins/jetpack-mu-wpcom-plugin/moon/jetpack\_vendor/automattic/jetpack-mu-wpcom/src/build/"};
//# sourceURL=jetpack-mu-wpcom-settings-js-before


rltInitialize( {"token":null,"iframeOrigins":["https:\/\/widgets.wp.com"]} );
//# sourceURL=rlt-proxy-js-after






























{"imports":{"@wordpress/interactivity":"https://s0.wp.com/wp-content/plugins/gutenberg-core/v23.0.1/build/modules/interactivity/index.min.js?m=1777049355i&ver=4d2a3a72c7410d548881"}}


.recentcomments a {
display: inline !important;
padding: 0 !important;
margin: 0 !important;
}
table.recentcommentsavatartop img.avatar, table.recentcommentsavatarend img.avatar {
border: 0px;
margin: 0;
}
table.recentcommentsavatartop a, table.recentcommentsavatarend a {
border: 0px !important;
background-color: transparent !important;
}
td.recentcommentsavatarend, td.recentcommentsavatartop {
padding: 0px 0px 1px 0px;
margin: 0px;
}
td.recentcommentstextend {
border: none !important;
padding: 0px 0px 2px 10px;
}
.rtl td.recentcommentstextend {
padding: 0px 10px 2px 0px;
}
td.recentcommentstexttop {
border: none;
padding: 0px 0px 0px 10px;
}
.rtl td.recentcommentstexttop {
padding: 0px 10px 0px 0px;
}


@font-face{font-family:Manrope;font-style:normal;font-weight:200 800;font-display:fallback;src:url('https://s0.wp.com/wp-content/themes/pub/twentytwentyfive/assets/fonts/manrope/Manrope-VariableFont\_wght.woff2') format('woff2');}
@font-face{font-family:"Fira Code";font-style:normal;font-weight:300 700;font-display:fallback;src:url('https://s0.wp.com/wp-content/themes/pub/twentytwentyfive/assets/fonts/fira-code/FiraCode-VariableFont\_wght.woff2') format('woff2');}







window.dataLayer = window.dataLayer || [];
function gtag() { dataLayer.push( arguments ); }
gtag( 'js', new Date() );
gtag( 'config', "G-32PC65RM90" );


[Skip to content](#wp--skip-link--target "#wp--skip-link--target")

[AB's Reflections](https://abaditya.com "https://abaditya.com")

+ [About me](https://abaditya.com/about/ "https://abaditya.com/about/")
+ [Contact](https://abaditya.com/contact/ "https://abaditya.com/contact/")

Subscribe

[Log in](https://wordpress.com/log-in/link?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fabaditya.com%252F2026%252F03%252F05%252Fthe-dark-factory-engineering-teams-that-run-with-the-lights-off%252F "https://wordpress.com/log-in/link?redirect_to=https%3A%2F%2Fr-login.wordpress.com%2Fremote-login.php%3Faction%3Dlink%26back%3Dhttps%253A%252F%252Fabaditya.com%252F2026%252F03%252F05%252Fthe-dark-factory-engineering-teams-that-run-with-the-lights-off%252F")



The Dark Factory: Engineering Teams That Run With the Lights Off
================================================================

Written by

[Aditya](https://abaditya.com/author/abaditya/ "https://abaditya.com/author/abaditya/")

in

[AI](https://abaditya.com/category/ai/ "https://abaditya.com/category/ai/"), [Programming](https://abaditya.com/category/programming/ "https://abaditya.com/category/programming/"), [Technology](https://abaditya.com/category/technology/ "https://abaditya.com/category/technology/"), [Thoughts](https://abaditya.com/category/thoughts/ "https://abaditya.com/category/thoughts/"), [Work](https://abaditya.com/category/work/ "https://abaditya.com/category/work/")

A few engineering organisations are already operating a model most companies haven’t begun to consider. While the typical software team debates whether to adopt AI coding assistants, companies like [StrongDM](https://factory.strongdm.ai/ "https://factory.strongdm.ai/") are running fully automated development pipelines where agents handle implementation, testing, review, and deployment. Humans set direction and define constraints. The mechanical work happens without them.

This isn’t speculative. It’s operational. And the gap between companies working this way and those that aren’t is widening fast.

What “lights off” actually means
--------------------------------

The term comes from manufacturing — factories that run autonomously, with minimal human presence. In software, it describes engineering organisations where AI agents do the bulk of execution work while humans focus on architecture, constraints, and outcomes.

StrongDM’s approach is instructive: their benchmark is that if you haven’t spent at least $1,000 on tokens per human engineer per day, your software factory has room for improvement. Agents work in parallel on isolated tasks. Code is written, tested, and reviewed without manual intervention. Tasks assigned Friday evening return results Monday morning.

The ratio of agents to humans is high and growing. But this isn’t about replacing engineers — it’s about fundamentally changing what engineers do.

The guardrails are the system
-----------------------------

Dark factories aren’t ungoverned. They’re heavily governed in a different way.

Linters, formatters, comprehensive test suites, design pattern enforcement — these become pre-conditions rather than suggestions. Agents are configured to seek completion only when all guardrails pass. Code review shifts from line-by-line human inspection to AI review with human spot-checks on critical paths.

The discipline moves from “write good code” to “design good systems for code to be written in.” That’s a different skill. It requires thinking about constraints, validation, and feedback loops rather than syntax and implementation details.

[Anthropic’s experiment](https://www.anthropic.com/engineering/building-c-compiler "https://www.anthropic.com/engineering/building-c-compiler") building a C compiler with parallel Claude instances demonstrates this principle. Sixteen agents worked simultaneously on a shared codebase, coordinating through git locks and comprehensive test harnesses. The result: a 100,000-line compiler capable of building the Linux kernel, produced over nearly 2,000 sessions across two weeks for just under $20,000. The project worked because the test infrastructure was rigorous enough to guide autonomous agents toward correctness without human review of every change.

[Cursor’s experiments with scaling agents](https://cursor.com/blog/scaling-agents "https://cursor.com/blog/scaling-agents") ran into a different problem. They tried flat coordination first — agents self-organising through a shared file, claiming tasks, updating status. It broke down. Agents held locks too long, became risk-averse, made small safe changes, and nobody took responsibility for hard problems. The fix was introducing hierarchy: planners that explore the codebase and create tasks, workers that grind on assigned work until it’s done. No single agent tries to do everything. The system ran for weeks, writing over a million lines of code. One project improved video rendering performance by 25x and shipped to production. Their takeaway: many of the gains came from removing complexity rather than adding it.

Digital twins as the enabler
----------------------------

The biggest blocker to agent autonomy has been the fear of breaking production. Digital twins remove that constraint.

StrongDM built behavioural replicas of third-party services their software depends on — Okta, Jira, Slack, Google Docs, Google Drive, and Google Sheets. These twins replicate APIs, edge cases, and observable behaviours with sufficient fidelity that agents can test against realistic conditions at volume, without rate limits or production risk.

[Simon Willison’s write-up](https://simonwillison.net/2026/Feb/7/software-factory/ "https://simonwillison.net/2026/Feb/7/software-factory/") of StrongDM’s approach highlights how this changed what was economically feasible: “Creating a high fidelity clone of a significant SaaS application was always possible, but never economically feasible. Generations of engineers may have wanted a full in-memory replica of their CRM to test against, but self-censored the proposal to build it.”

What makes this rigorous rather than just better staging is how they handle validation. Test scenarios are stored outside the codebase — separate from where the coding agents can see them — functioning like holdout sets in machine learning. Agents can’t overfit to the tests because they don’t have access to them. The QA team is also agents, running thousands of scenarios per hour without hitting rate limits or accumulating API costs.

The structural advantage of starting fresh
------------------------------------------

Startups and SMBs have a material advantage here. No legacy organisational structure to dismantle. No 500-person engineering floor with stakeholders defending headcount. No 18-month procurement cycles.

Capital efficiency becomes native. A three-person team with agents can produce output that previously required twenty people. The cost of compute is a fraction of equivalent human labour and falling rapidly.

This creates an asymmetric advantage. If your competitor ships in days what takes you months, no amount of talent closes that gap. And the competitive pressure isn’t just on speed — it’s on the ability to attract talent that wants to work this way. Senior engineers who’ve experienced agent-driven development don’t want to go back to manual workflows.

The gap between adopters and laggards
-------------------------------------

Companies operating this way are shipping at a fundamentally different pace. The difference isn’t incremental — it’s orders of magnitude in output per person.

Block’s recent announcement of a [near-50% reduction in headcount](https://x.com/jack/status/2027129697092731343 "https://x.com/jack/status/2027129697092731343") offers a data point. The company is reducing its organization from over 10,000 people to just under 6,000. Jack Dorsey stated “we’re not making this decision because we’re in trouble. our business is strong” but noted that “the intelligence tools we’re creating and using, paired with smaller and flatter teams, are enabling a new way of working which fundamentally changes what it means to build and run a company.”

[Cursor’s data](https://x.com/mntruell/status/2026736314272591924 "https://x.com/mntruell/status/2026736314272591924") shows the same pattern. 35% of pull requests merged internally at Cursor are now created by agents operating autonomously in cloud VMs. The developers adopting this approach write almost no code themselves. They spend their time breaking down problems, reviewing artifacts, and giving feedback. They spin up multiple agents simultaneously instead of guiding one to completion.

The laggards aren’t just slower. They’re increasingly unable to compete for talent, capital, or market position against organisations that have made this transition.

You don’t need a corporate budget to start
------------------------------------------

The dark factory model scales down. A single developer with a Claude Code subscription and well-structured GitHub workflows can run a lightweight version of the same approach.

Start with one workflow. Pick a repetitive part of your development or business process, establish the guardrails, and let agents handle it. The key investment isn’t in compute — it’s in guardrails and context. Linters, test suites, good documentation, and clear specifications matter more than token budget.

For SMBs and founders, this is the most asymmetric advantage available. You can operate at a scale that was previously only accessible with significant headcount. The learning curve is steep but short. Within 30 days of serious experimentation, most people develop the intuition for what agents can and can’t handle.

Projects like [OpenClaw](https://openclaw.ai/ "https://openclaw.ai/") — an open-source autonomous agent that executes tasks across messaging platforms and services — demonstrate that the tooling for this approach is increasingly accessible. The software runs locally, integrates with multiple LLM providers, and requires no enterprise licensing. The barrier isn’t access to technology. It’s willingness to change how work gets done.

What this means beyond software
-------------------------------

Software is where this pattern is playing out first, but the model applies wherever knowledge work is structured and repeatable.

Audit processes. Compliance checks. Report generation. Data analysis. Document review. These are all candidates for the same approach: clear specifications, comprehensive validation, and autonomous execution within defined guardrails.

Most traditional industries haven’t started thinking about this. They’re still debating whether to use ChatGPT for email drafts. The firms that figure out how to apply dark factory principles to their domain will have an enormous advantage over those still operating with manual workflows.

The lights are already off in some factories. The question isn’t whether this approach will spread. It’s how quickly your organisation recognises that the game has changed.

### Share:

* [Share on WhatsApp (Opens in new window)
  WhatsApp](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=jetpack-whatsapp "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=jetpack-whatsapp")
* [Share on X (Opens in new window)
  X](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=x "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=x")
* [Share on Facebook (Opens in new window)
  Facebook](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=facebook "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=facebook")
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=linkedin "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=linkedin")
* [Email a link to a friend (Opens in new window)
  Email](mailto:?subject=%5BShared%20Post%5D%20The%20Dark%20Factory%3A%20Engineering%20Teams%20That%20Run%20With%20the%20Lights%20Off&body=https%3A%2F%2Fabaditya.com%2F2026%2F03%2F05%2Fthe-dark-factory-engineering-teams-that-run-with-the-lights-off%2F&share=email "mailto:?subject=%5BShared%20Post%5D%20The%20Dark%20Factory%3A%20Engineering%20Teams%20That%20Run%20With%20the%20Lights%20Off&body=https%3A%2F%2Fabaditya.com%2F2026%2F03%2F05%2Fthe-dark-factory-engineering-teams-that-run-with-the-lights-off%2F&share=email")
* [Print (Opens in new window)
  Print](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/#print?share=print "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/#print?share=print")
* [More](# "#")

* [Share on Threads (Opens in new window)
  Threads](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=threads "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=threads")
* [Share on Bluesky (Opens in new window)
  Bluesky](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=bluesky "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=bluesky")
* [Share on Reddit (Opens in new window)
  Reddit](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=reddit "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=reddit")
* [Share on Pinterest (Opens in new window)
  Pinterest](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=pinterest "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?share=pinterest")

Like Loading…

---

### Discover more from AB's Reflections

Subscribe to get the latest posts sent to your email.

Type your email…

Subscribe

[AI](https://abaditya.com/tag/ai/ "https://abaditya.com/tag/ai/") [engineer](https://abaditya.com/tag/engineer/ "https://abaditya.com/tag/engineer/") [enterprise](https://abaditya.com/tag/enterprise/ "https://abaditya.com/tag/enterprise/") [factory](https://abaditya.com/tag/factory/ "https://abaditya.com/tag/factory/") [futureofwork](https://abaditya.com/tag/futureofwork/ "https://abaditya.com/tag/futureofwork/") [organization](https://abaditya.com/tag/organization/ "https://abaditya.com/tag/organization/") [Technology](https://abaditya.com/tag/technology/ "https://abaditya.com/tag/technology/") [The Great Rebalancing](https://abaditya.com/tag/the-great-rebalancing/ "https://abaditya.com/tag/the-great-rebalancing/") [thoughts](https://abaditya.com/tag/thoughts-2/ "https://abaditya.com/tag/thoughts-2/") [vibe coding](https://abaditya.com/tag/vibe-coding/ "https://abaditya.com/tag/vibe-coding/")

←[The Judgment Bottleneck: Why Direction Matters More Than Execution Speed](https://abaditya.com/2026/03/03/the-judgment-bottleneck-why-direction-matters-more-than-execution-speed/ "https://abaditya.com/2026/03/03/the-judgment-bottleneck-why-direction-matters-more-than-execution-speed/")

[The Task Changed, The Job Didn’t — But Your Org Hasn’t Noticed Yet](https://abaditya.com/2026/03/10/the-task-changed-the-job-didnt-but-your-org-hasnt-noticed-yet/ "https://abaditya.com/2026/03/10/the-task-changed-the-job-didnt-but-your-org-hasnt-noticed-yet/")→

Comments
--------

### 3 responses to “The Dark Factory: Engineering Teams That Run With the Lights Off”

1. [March 12, 2026](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37391 "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37391")

   [The Autonomous SDLC: What’s Solved, What’s Not, and Why the Gaps Are Closing Fast – AB's Reflections](https://abaditya.com/2026/03/12/the-autonomous-sdlc-whats-solved-whats-not-and-why-the-gaps-are-closing-fast/ "https://abaditya.com/2026/03/12/the-autonomous-sdlc-whats-solved-whats-not-and-why-the-gaps-are-closing-fast/")

   […] took this further with their dark factory approach. They built digital twins of production dependencies—behavioral clones of Okta, Jira, […]

   [Like](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37391&_wpnonce=4edcb64c04 "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37391&_wpnonce=4edcb64c04")Like
2. [March 17, 2026](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37395 "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37395")

   [Indian IT’s Arbitrage Problem: When Tokens Cost the Same Everywhere – AB's Reflections](https://abaditya.com/2026/03/17/indian-its-arbitrage-problem-when-tokens-cost-the-same-everywhere/ "https://abaditya.com/2026/03/17/indian-its-arbitrage-problem-when-tokens-cost-the-same-everywhere/")

   […] same forces dismantling labour arbitrage are creating opportunities for lean operators. A solo developer or small team with the right domain expertise and AI tools can now deliver enterprise-grade output. Clients don’t care if the work was done […]

   [Like](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37395&_wpnonce=73a4f88c8e "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37395&_wpnonce=73a4f88c8e")Like
3. [March 19, 2026](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37398 "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/comment-page-1/#comment-37398")

   [The AI Stack Is Running on Borrowed Infrastructure — And What Happens When It Isn’t – AB's Reflections](https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/ "https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/")

   […] of that is a reason to wait. Dark factory teams are already running production workflows on the borrowed stack — and the gap between them and […]

   [Like](https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37398&_wpnonce=e2eb8de3da "https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/?like_comment=37398&_wpnonce=e2eb8de3da")Like

More posts
----------

* ### [What it takes to actually run NanoClaw](https://abaditya.com/2026/05/06/what-it-takes-to-actually-run-nanoclaw/ "https://abaditya.com/2026/05/06/what-it-takes-to-actually-run-nanoclaw/")

  [May 6, 2026](https://abaditya.com/2026/05/06/what-it-takes-to-actually-run-nanoclaw/ "https://abaditya.com/2026/05/06/what-it-takes-to-actually-run-nanoclaw/")
* ### [Why I picked NanoClaw over OpenClaw for a GTM pipeline](https://abaditya.com/2026/05/06/why-i-picked-nanoclaw-over-openclaw-for-a-gtm-pipeline/ "https://abaditya.com/2026/05/06/why-i-picked-nanoclaw-over-openclaw-for-a-gtm-pipeline/")

  [May 6, 2026](https://abaditya.com/2026/05/06/why-i-picked-nanoclaw-over-openclaw-for-a-gtm-pipeline/ "https://abaditya.com/2026/05/06/why-i-picked-nanoclaw-over-openclaw-for-a-gtm-pipeline/")
* ### [Building a GTM dark factory with Nemotron 3 and NanoClaw](https://abaditya.com/2026/05/06/building-a-gtm-dark-factory-with-nemotron-3-and-nanoclaw/ "https://abaditya.com/2026/05/06/building-a-gtm-dark-factory-with-nemotron-3-and-nanoclaw/")

  [May 6, 2026](https://abaditya.com/2026/05/06/building-a-gtm-dark-factory-with-nemotron-3-and-nanoclaw/ "https://abaditya.com/2026/05/06/building-a-gtm-dark-factory-with-nemotron-3-and-nanoclaw/")
* ### [The AI Stack Is Running on Borrowed Infrastructure — And What Happens When It Isn’t](https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/ "https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/")

  [March 19, 2026](https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/ "https://abaditya.com/2026/03/19/the-ai-stack-is-running-on-borrowed-infrastructure-and-what-happens-when-it-isnt/")



[AB's Reflections](https://abaditya.com "https://abaditya.com")

Geeky thoughts on a variety of topics

[Website Powered by WordPress.com](https://wordpress.com/?ref=footer_custom_powered "https://wordpress.com/?ref=footer_custom_powered").


{"prefetch":[{"source":"document","where":{"and":[{"href\_matches":"/\*"},{"not":{"href\_matches":["/wp-\*.php","/wp-admin/\*","/files/\*","/wp-content/\*","/wp-content/plugins/\*","/wp-content/themes/pub/twentytwentyfive/\*","/\*\\?(.+)"]}},{"not":{"selector\_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector\_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}

Discover more from AB's Reflections
-----------------------------------

Subscribe now to keep reading and get access to the full archive.

Type your email…

Subscribe

[Continue reading](# "#")

Subscribe



var WPGroHo = {"my\_hash":""};
//# sourceURL=wpgroho-js-extra


// Initialize and attach hovercards to all gravatars
( function() {
function init() {
if ( typeof Gravatar === 'undefined' ) {
return;
}
if ( typeof Gravatar.init !== 'function' ) {
return;
}
Gravatar.profile\_cb = function ( hash, id ) {
WPGroHo.syncProfileData( hash, id );
};
Gravatar.my\_hash = WPGroHo.my\_hash;
Gravatar.init(
'body',
'#wp-admin-bar-my-account',
{
i18n: {
'Edit your profile →': 'Edit your profile →',
'View profile →': 'View profile →',
'Contact': 'Contact',
'Send money': 'Send money',
'Sorry, we are unable to load this Gravatar profile.': 'Sorry, we are unable to load this Gravatar profile.',
'Gravatar not found.': 'Gravatar not found.',
'Too Many Requests.': 'Too Many Requests.',
'Internal Server Error.': 'Internal Server Error.',
'Is this you?': 'Is this you?',
'Claim your free profile.': 'Claim your free profile.',
'Email': 'Email',
'Home Phone': 'Home Phone',
'Work Phone': 'Work Phone',
'Cell Phone': 'Cell Phone',
'Contact Form': 'Contact Form',
'Calendar': 'Calendar',
},
}
);
}
if ( document.readyState !== 'loading' ) {
init();
} else {
document.addEventListener( 'DOMContentLoaded', init );
}
} )();
window.WPCOM\_sharing\_counts = {"https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/":7826};





var Jetpack\_Subscriptions = {"modalLoadTime":"60000","modalScrollThreshold":"50","modalInterval":"86400000"};
//# sourceURL=subscribe-modal-js-js-extra

var comment\_like\_text = {"loading":"Loading...","swipeUrl":"https://s0.wp.com/wp-content/mu-plugins/comment-likes/js/lib/swipe.js?m=1382645497i&amp;ver=20131008"};
//# sourceURL=comment-like-js-extra

var sharing\_js\_options = {"lang":"en","counts":"1","is\_stats\_active":"1"};
//# sourceURL=sharing-js-js-extra


var windowOpen;
( function () {
function matches( el, sel ) {
return !! (
el.matches && el.matches( sel ) ||
el.msMatchesSelector && el.msMatchesSelector( sel )
);
}
document.body.addEventListener( 'click', function ( event ) {
if ( ! event.target ) {
return;
}
var el;
if ( matches( event.target, 'a.share-x' ) ) {
el = event.target;
} else if ( event.target.parentNode && matches( event.target.parentNode, 'a.share-x' ) ) {
el = event.target.parentNode;
}
if ( el ) {
event.preventDefault();
// If there's another sharing window open, close it.
if ( typeof windowOpen !== 'undefined' ) {
windowOpen.close();
}
windowOpen = window.open( el.getAttribute( 'href' ), 'wpcomx', 'menubar=1,resizable=1,width=600,height=350' );
return false;
}
} );
} )();
var windowOpen;
( function () {
function matches( el, sel ) {
return !! (
el.matches && el.matches( sel ) ||
el.msMatchesSelector && el.msMatchesSelector( sel )
);
}
document.body.addEventListener( 'click', function ( event ) {
if ( ! event.target ) {
return;
}
var el;
if ( matches( event.target, 'a.share-facebook' ) ) {
el = event.target;
} else if ( event.target.parentNode && matches( event.target.parentNode, 'a.share-facebook' ) ) {
el = event.target.parentNode;
}
if ( el ) {
event.preventDefault();
// If there's another sharing window open, close it.
if ( typeof windowOpen !== 'undefined' ) {
windowOpen.close();
}
windowOpen = window.open( el.getAttribute( 'href' ), 'wpcomfacebook', 'menubar=1,resizable=1,width=600,height=400' );
return false;
}
} );
} )();
var windowOpen;
( function () {
function matches( el, sel ) {
return !! (
el.matches && el.matches( sel ) ||
el.msMatchesSelector && el.msMatchesSelector( sel )
);
}
document.body.addEventListener( 'click', function ( event ) {
if ( ! event.target ) {
return;
}
var el;
if ( matches( event.target, 'a.share-linkedin' ) ) {
el = event.target;
} else if ( event.target.parentNode && matches( event.target.parentNode, 'a.share-linkedin' ) ) {
el = event.target.parentNode;
}
if ( el ) {
event.preventDefault();
// If there's another sharing window open, close it.
if ( typeof windowOpen !== 'undefined' ) {
windowOpen.close();
}
windowOpen = window.open( el.getAttribute( 'href' ), 'wpcomlinkedin', 'menubar=1,resizable=1,width=580,height=450' );
return false;
}
} );
} )();
var windowOpen;
( function () {
function matches( el, sel ) {
return !! (
el.matches && el.matches( sel ) ||
el.msMatchesSelector && el.msMatchesSelector( sel )
);
}
document.body.addEventListener( 'click', function ( event ) {
if ( ! event.target ) {
return;
}
var el;
if ( matches( event.target, 'a.share-threads' ) ) {
el = event.target;
} else if ( event.target.parentNode && matches( event.target.parentNode, 'a.share-threads' ) ) {
el = event.target.parentNode;
}
if ( el ) {
event.preventDefault();
// If there's another sharing window open, close it.
if ( typeof windowOpen !== 'undefined' ) {
windowOpen.close();
}
windowOpen = window.open( el.getAttribute( 'href' ), 'wpcomthreads', 'menubar=1,resizable=1,width=600,height=400' );
return false;
}
} );
} )();
var windowOpen;
( function () {
function matches( el, sel ) {
return !! (
el.matches && el.matches( sel ) ||
el.msMatchesSelector && el.msMatchesSelector( sel )
);
}
document.body.addEventListener( 'click', function ( event ) {
if ( ! event.target ) {
return;
}
var el;
if ( matches( event.target, 'a.share-bluesky' ) ) {
el = event.target;
} else if ( event.target.parentNode && matches( event.target.parentNode, 'a.share-bluesky' ) ) {
el = event.target.parentNode;
}
if ( el ) {
event.preventDefault();
// If there's another sharing window open, close it.
if ( typeof windowOpen !== 'undefined' ) {
windowOpen.close();
}
windowOpen = window.open( el.getAttribute( 'href' ), 'wpcombluesky', 'menubar=1,resizable=1,width=600,height=400' );
return false;
}
} );
} )();
//# sourceURL=sharing-js-js-after

<!--//--><![CDATA[//><!--
PDRTJS\_settings\_214830\_comm\_37391={"id":214830,"unique\_id":"wp-comment-37391","title":"%26%23091%3B%26%238230%3B%26%23093%3B%20took%20this%20further%20with%20their%20dark%20factory%20approach.%20They%20built%20digital%20twins%20of%20production%20dependenciesbehavioral%20clones%20of%20Okta%2C%20Jira%2C%20%26%23091%3B%26%238230%3B%26%23093%3B...","permalink":"https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/#comment-37391","item\_id":"\_comm\_37391"}; if ( typeof PDRTJS\_RATING !== 'undefined' ){if ( typeof PDRTJS\_214830\_comm\_37391 == 'undefined' ){PDRTJS\_214830\_comm\_37391 = new PDRTJS\_RATING( PDRTJS\_settings\_214830\_comm\_37391 );}}PDRTJS\_settings\_214830\_comm\_37395={"id":214830,"unique\_id":"wp-comment-37395","title":"%26%23091%3B%26%238230%3B%26%23093%3B%20same%20forces%20dismantling%20labour%20arbitrage%20are%20creating%20opportunities%20for%20lean%20operators.%20A%20solo%20developer%20or%20small%20team%20with%20the%20right%20domain%20expertise%20and%20AI%20tools%20can%20now%20deliver%20enter...","permalink":"https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/#comment-37395","item\_id":"\_comm\_37395"}; if ( typeof PDRTJS\_RATING !== 'undefined' ){if ( typeof PDRTJS\_214830\_comm\_37395 == 'undefined' ){PDRTJS\_214830\_comm\_37395 = new PDRTJS\_RATING( PDRTJS\_settings\_214830\_comm\_37395 );}}PDRTJS\_settings\_214830\_comm\_37398={"id":214830,"unique\_id":"wp-comment-37398","title":"%26%23091%3B%26%238230%3B%26%23093%3B%20of%20that%20is%20a%20reason%20to%20wait.%20Dark%20factory%20teams%20are%20already%20running%20production%20workflows%20on%20the%20borrowed%20stack%20%20and%20the%20gap%20between%20them%20and%20%26%23091%3B%26%238230%3B%26%23093%3B...","permalink":"https://abaditya.com/2026/03/05/the-dark-factory-engineering-teams-that-run-with-the-lights-off/#comment-37398","item\_id":"\_comm\_37398"}; if ( typeof PDRTJS\_RATING !== 'undefined' ){if ( typeof PDRTJS\_214830\_comm\_37398 == 'undefined' ){PDRTJS\_214830\_comm\_37398 = new PDRTJS\_RATING( PDRTJS\_settings\_214830\_comm\_37398 );}}
//--><!]]>
//# sourceURL=crowdsignal-rating-js-before


(function () {
var wpcom\_reblog = {
source: 'toolbar',
toggle\_reblog\_box\_flair: function (obj\_id, post\_id) {
// Go to site selector. This will redirect to their blog if they only have one.
const postEndpoint = `https://wordpress.com/post`;
// Ideally we would use the permalink here, but fortunately this will be replaced with the
// post permalink in the editor.
const originalURL = `${ document.location.href }?page\_id=${ post\_id }`;
const url =
postEndpoint +
'?url=' +
encodeURIComponent( originalURL ) +
'&is\_post\_share=true' +
'&v=5';
const redirect = function () {
if (
! window.open( url, '\_blank' )
) {
location.href = url;
}
};
if ( /Firefox/.test( navigator.userAgent ) ) {
setTimeout( redirect, 0 );
} else {
redirect();
}
},
};
window.wpcom\_reblog = wpcom\_reblog;
})();

{"baseUrl":"https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/","ext":".png","svgUrl":"https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/svg/","svgExt":".svg","source":{"concatemoji":"/wp-includes/js/wp-emoji-release.min.js?m=1764078722i&ver=7.0-RC2-62280"}}

/\*! This file is auto-generated \*/
const a=JSON.parse(document.getElementById("wp-emoji-settings").textContent),o=(window.\_wpemojiSettings=a,"wpEmojiSettingsSupports"),s=["flag","emoji"];function i(e){try{var t={supportTests:e,timestamp:(new Date).valueOf()};sessionStorage.setItem(o,JSON.stringify(t))}catch(e){}}function c(e,t,n){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);t=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data);e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(n,0,0);const a=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data);return t.every((e,t)=>e===a[t])}function p(e,t){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);var n=e.getImageData(16,16,1,1);for(let e=0;e<n.data.length;e++)if(0!==n.data[e])return!1;return!0}function u(e,t,n,a){switch(t){case"flag":return n(e,"\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!n(e,"\ud83c\udde8\ud83c\uddf6","\ud83c\udde8\u200b\ud83c\uddf6")&&!n(e,"\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!a(e,"\ud83e\u1fac8")}return!1}function f(e,t,n,a){let r;const o=(r="undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?new OffscreenCanvas(300,150):document.createElement("canvas")).getContext("2d",{willReadFrequently:!0}),s=(o.textBaseline="top",o.font="600 32px Arial",{});return e.forEach(e=>{s[e]=t(o,e,n,a)}),s}function r(e){var t=document.createElement("script");t.src=e,t.defer=!0,document.head.appendChild(t)}a.supports={everything:!0,everythingExceptFlag:!0},new Promise(t=>{let n=function(){try{var e=JSON.parse(sessionStorage.getItem(o));if("object"==typeof e&&"number"==typeof e.timestamp&&(new Date).valueOf()<e.timestamp+604800&&"object"==typeof e.supportTests)return e.supportTests}catch(e){}return null}();if(!n){if("undefined"!=typeof Worker&&"undefined"!=typeof OffscreenCanvas&&"undefined"!=typeof URL&&URL.createObjectURL&&"undefined"!=typeof Blob)try{var e="postMessage("+f.toString()+"("+[JSON.stringify(s),u.toString(),c.toString(),p.toString()].join(",")+"));",a=new Blob([e],{type:"text/javascript"});const r=new Worker(URL.createObjectURL(a),{name:"wpTestEmojiSupports"});return void(r.onmessage=e=>{i(n=e.data),r.terminate(),t(n)})}catch(e){}i(n=f(s,u,c,p))}t(n)}).then(e=>{for(const n in e)a.supports[n]=e[n],a.supports.everything=a.supports.everything&&a.supports[n],"flag"!==n&&(a.supports.everythingExceptFlag=a.supports.everythingExceptFlag&&a.supports[n]);var t;a.supports.everythingExceptFlag=a.supports.everythingExceptFlag&&!a.supports.flag,a.supports.everything||((t=a.source||{}).concatemoji?r(t.concatemoji):t.wpemoji&&t.twemoji&&(r(t.twemoji),r(t.wpemoji)))});
//# sourceURL=/wp-includes/js/wp-emoji-loader.min.js


%d

 
\_tkq = window.\_tkq || [];
\_stq = window.\_stq || [];
\_tkq.push(['storeContext', {'blog\_id':'62550','blog\_tz':'5','user\_lang':'en','blog\_lang':'en','user\_id':'0'}]);
// Prevent sending pageview tracking from WP-Admin pages.
\_stq.push(['view', {'blog':'62550','v':'wpcom','tz':'5','user\_id':'0','post':'7826','subd':'abaditya'}]);
\_stq.push(['extra', {'crypt':'UE5tW3cvZGQ/JUs1UEpSdi1dRV9aa1lnfD1uUXIwSiVJWUhGdEswb1suUC5SUUtoai5BZUgrK0c0K2Rkek1BLGJXWGszLFZWUXQwQ1JPLGlGWjRudVF4Ly1HdjQtK1ZpZGJWZ05XYzlLeC1xUGF4UFFPbz9ZbVgxMFNtNTUuem9BUTNOU01+U2REJnpQcjFjMjVZJVpVP3kvb1JYXW4wQVhpNTQrbVh8M1NSeTcvOHNPcUFYYS1Ncl95PWNWRSVkdCtzeTVVYWdSZ0kwNSw3REVfaXMtLjQyZzlla05mQ2FCWkNf'}]);
\_stq.push([ 'clickTrackerInit', '62550', '7826' ]);
