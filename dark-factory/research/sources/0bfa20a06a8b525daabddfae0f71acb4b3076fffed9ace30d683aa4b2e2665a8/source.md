# Docker — Deterministic AI Testing with Session Recording in cagent

Source: https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/

---

(window.NREUM||(NREUM={})).init={privacy:{cookies\_enabled:true},ajax:{deny\_list:["bam.nr-data.net"]},feature\_flags:["soft\_nav"],distributed\_tracing:{enabled:true}};(window.NREUM||(NREUM={})).loader\_config={agentID:"1386242466",accountID:"6399396",trustKey:"6399396",xpid:"UgUOWFVaDhABVlRWBgMEVVMI",licenseKey:"NRJS-27f33ade91093c8b2a2",applicationID:"1254123379",browserID:"1386242466"};;/\*! For license information please see nr-loader-spa-1.314.0.min.js.LICENSE.txt \*/
(()=>{var e,t,r={384:(e,t,r)=>{"use strict";r.d(t,{NT:()=>a,Zm:()=>c,bQ:()=>u,dV:()=>d,pV:()=>l});var n=r(6154),i=r(1863),s=r(944),o=r(1910);const a={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net"};function c(){return n.gm.NREUM||(n.gm.NREUM={}),void 0===n.gm.newrelic&&(n.gm.newrelic=n.gm.NREUM),n.gm.NREUM}function d(){let e=c();return e.o||(e.o={ST:n.gm.setTimeout,SI:n.gm.setImmediate||n.gm.setInterval,CT:n.gm.clearTimeout,XHR:n.gm.XMLHttpRequest,REQ:n.gm.Request,EV:n.gm.Event,PR:n.gm.Promise,MO:n.gm.MutationObserver,FETCH:n.gm.fetch,WS:n.gm.WebSocket},(0,o.i)(...Object.values(e.o))),e}function u(e,t){let r=c();r.initializedAgents??={},t.initializedAt={ms:(0,i.t)(),date:new Date},r.initializedAgents[e]=t,2===Object.keys(r.initializedAgents).length&&(0,s.R)(69)}function l(){return function(){let e=c();const t=e.info||{};e.info={beacon:a.beacon,errorBeacon:a.errorBeacon,...t}}(),function(){let e=c();const t=e.init||{};e.init={...t}}(),d(),function(){let e=c();const t=e.loader\_config||{};e.loader\_config={...t}}(),c()}},782:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.pageViewTiming},860:(e,t,r)=>{"use strict";r.d(t,{$J:()=>u,K7:()=>c,P3:()=>d,XX:()=>i,Yy:()=>a,df:()=>s,qY:()=>n,v4:()=>o});const n="events",i="jserrors",s="browser/blobs",o="rum",a="browser/logs",c={ajax:"ajax",genericEvents:"generic\_events",jserrors:i,logging:"logging",metrics:"metrics",pageAction:"page\_action",pageViewEvent:"page\_view\_event",pageViewTiming:"page\_view\_timing",sessionReplay:"session\_replay",sessionTrace:"session\_trace",softNav:"soft\_navigations"},d={[c.pageViewEvent]:1,[c.pageViewTiming]:2,[c.metrics]:3,[c.jserrors]:4,[c.softNav]:5,[c.ajax]:6,[c.sessionTrace]:7,[c.sessionReplay]:8,[c.logging]:9,[c.genericEvents]:10},u={[c.pageViewEvent]:o,[c.pageViewTiming]:n,[c.ajax]:n,[c.softNav]:n,[c.metrics]:i,[c.jserrors]:i,[c.sessionTrace]:s,[c.sessionReplay]:s,[c.logging]:a,[c.genericEvents]:"ins"}},944:(e,t,r)=>{"use strict";r.d(t,{R:()=>i});var n=r(3241);function i(e,t){"function"==typeof console.debug&&(console.debug("New Relic Warning: https://github.com/newrelic/newrelic-browser-agent/blob/main/docs/warning-codes.md#".concat(e),t),(0,n.W)({drained:null,type:"data",name:"warn",feature:"warn",data:{code:e,secondary:t}}))}},993:(e,t,r)=>{"use strict";r.d(t,{A$:()=>s,ET:()=>o,TZ:()=>a,p\_:()=>i});var n=r(860);const i={ERROR:"ERROR",WARN:"WARN",INFO:"INFO",DEBUG:"DEBUG",TRACE:"TRACE"},s={OFF:0,ERROR:1,WARN:2,INFO:3,DEBUG:4,TRACE:5},o="log",a=n.K7.logging},1687:(e,t,r)=>{"use strict";r.d(t,{Ak:()=>a,Ze:()=>d,x3:()=>c});var n=r(3241),i=r(3606),s=r(860),o=r(2646);function a(e,t){if(!e)return;const r={staged:!1,priority:s.P3[t]||0};e.runtime.drainRegistry.get(t)||e.runtime.drainRegistry.set(t,r)}function c(e,t){if(!e)return;const r=e.runtime.drainRegistry;r&&(r.get(t)&&r.delete(t),l(e,t,!1),r.size&&u(e))}function d(e,t="feature",r=!1){if(e){if(!e.runtime.drainRegistry.get(t)||r)return l(e,t);e.runtime.drainRegistry.get(t).staged=!0,u(e)}}function u(e){if(!e)return;const t=Array.from(e.runtime.drainRegistry);t.every(([e,t])=>t.staged)&&(t.sort((e,t)=>e[1].priority-t[1].priority),t.forEach(([t])=>{e.runtime.drainRegistry.delete(t),l(e,t)}))}function l(e,t,r=!0){if(!e)return;const s=e.ee,a=i.i.handlers;if(s&&!s.aborted&&s.backlog&&a){if((0,n.W)({type:"lifecycle",name:"drain",feature:t}),r){const e=s.backlog[t],r=a[t];if(r){for(let t=0;e&&t<e.length;++t)f(e[t],r);Object.entries(r).forEach(([e,t])=>{Object.values(t||{}).forEach(t=>{t[0]?.on&&t[0].context()instanceof o.y&&!t[0].listeners(e).includes(t[1])&&t[0].on(e,t[1])})})}}s.isolatedBacklog||delete a[t],s.backlog[t]=null,s.emit("drain-"+t,[])}}function f(e,t){var r=e[1];Object.values(t[r]||{}).forEach(t=>{var r=e[0];if(t[0]===r){var n=t[1],i=e[3],s=e[2];n.apply(i,s)}})}},1738:(e,t,r)=>{"use strict";r.d(t,{U:()=>f,Y:()=>l});var n=r(3241),i=r(9908),s=r(1863),o=r(944),a=r(3969),c=r(8362),d=r(860),u=r(4261);function l(e,t,r,s){const l=s||r;!l||l[e]&&l[e]!==c.d.prototype[e]||(l[e]=function(){(0,i.p)(a.xV,["API/"+e+"/called"],void 0,d.K7.metrics,r.ee),(0,n.W)({drained:!!r.runtime?.activatedFeatures,type:"data",name:"api",feature:u.Pl+e,data:{}});try{return t.apply(this,arguments)}catch(e){(0,o.R)(23,e)}})}function f(e,t,r,n,o){const a=e.info;null===r?delete a.jsAttributes[t]:a.jsAttributes[t]=r,(o||null===r)&&(0,i.p)(u.Pl+n,[(0,s.t)(),t,r],void 0,"session",e.ee)}},1741:(e,t,r)=>{"use strict";r.d(t,{W:()=>s});var n=r(944),i=r(4261);class s{#e(e,...t){if(this[e]!==s.prototype[e])return this[e](...t);(0,n.R)(35,e)}addPageAction(e,t){return this.#e(i.hG,e,t)}register(e){return this.#e(i.eY,e)}recordCustomEvent(e,t){return this.#e(i.fF,e,t)}setPageViewName(e,t){return this.#e(i.Fw,e,t)}setCustomAttribute(e,t,r){return this.#e(i.cD,e,t,r)}noticeError(e,t){return this.#e(i.o5,e,t)}setUserId(e,t=!1){return this.#e(i.Dl,e,t)}setApplicationVersion(e){return this.#e(i.nb,e)}setErrorHandler(e){return this.#e(i.bt,e)}addRelease(e,t){return this.#e(i.k6,e,t)}log(e,t){return this.#e(i.$9,e,t)}start(){return this.#e(i.d3)}finished(e){return this.#e(i.BL,e)}recordReplay(){return this.#e(i.CH)}pauseReplay(){return this.#e(i.Tb)}addToTrace(e){return this.#e(i.U2,e)}setCurrentRouteName(e){return this.#e(i.PA,e)}interaction(e){return this.#e(i.dT,e)}wrapLogger(e,t,r){return this.#e(i.Wb,e,t,r)}measure(e,t){return this.#e(i.V1,e,t)}consent(e){return this.#e(i.Pv,e)}}},1863:(e,t,r)=>{"use strict";function n(){return Math.floor(performance.now())}r.d(t,{t:()=>n})},1910:(e,t,r)=>{"use strict";r.d(t,{i:()=>s});var n=r(944);const i=new Map;function s(...e){return e.every(e=>{if(i.has(e))return i.get(e);const t="function"==typeof e?e.toString():"",r=t.includes("[native code]"),s=t.includes("nrWrapper");return r||s||(0,n.R)(64,e?.name||t),i.set(e,r),r})}},2555:(e,t,r)=>{"use strict";r.d(t,{D:()=>a,f:()=>o});var n=r(384),i=r(8122);const s={beacon:n.NT.beacon,errorBeacon:n.NT.errorBeacon,licenseKey:void 0,applicationID:void 0,sa:void 0,queueTime:void 0,applicationTime:void 0,ttGuid:void 0,user:void 0,account:void 0,product:void 0,extra:void 0,jsAttributes:{},userAttributes:void 0,atts:void 0,transactionName:void 0,tNamePlain:void 0};function o(e){try{return!!e.licenseKey&&!!e.errorBeacon&&!!e.applicationID}catch(e){return!1}}const a=e=>(0,i.a)(e,s)},2614:(e,t,r)=>{"use strict";r.d(t,{BB:()=>o,H3:()=>n,g:()=>d,iL:()=>c,tS:()=>a,uh:()=>i,wk:()=>s});const n="NRBA",i="SESSION",s=144e5,o=18e5,a={STARTED:"session-started",PAUSE:"session-pause",RESET:"session-reset",RESUME:"session-resume",UPDATE:"session-update"},c={SAME\_TAB:"same-tab",CROSS\_TAB:"cross-tab"},d={OFF:0,FULL:1,ERROR:2}},2646:(e,t,r)=>{"use strict";r.d(t,{y:()=>n});class n{constructor(e){this.contextId=e}}},2843:(e,t,r)=>{"use strict";r.d(t,{G:()=>s,u:()=>i});var n=r(3878);function i(e,t=!1,r,i){(0,n.DD)("visibilitychange",function(){if(t)return void("hidden"===document.visibilityState&&e());e(document.visibilityState)},r,i)}function s(e,t,r){(0,n.sp)("pagehide",e,t,r)}},3241:(e,t,r)=>{"use strict";r.d(t,{W:()=>s});var n=r(6154);const i="newrelic";function s(e={}){try{n.gm.dispatchEvent(new CustomEvent(i,{detail:e}))}catch(e){}}},3304:(e,t,r)=>{"use strict";r.d(t,{A:()=>s});var n=r(7836);const i=()=>{const e=new WeakSet;return(t,r)=>{if("object"==typeof r&&null!==r){if(e.has(r))return;e.add(r)}return r}};function s(e){try{return JSON.stringify(e,i())??""}catch(e){try{n.ee.emit("internal-error",[e])}catch(e){}return""}}},3333:(e,t,r)=>{"use strict";r.d(t,{$v:()=>u,TZ:()=>n,Xh:()=>c,Zp:()=>i,kd:()=>d,mq:()=>a,nf:()=>o,qN:()=>s});const n=r(860).K7.genericEvents,i=["auxclick","click","copy","keydown","paste","scrollend"],s=["focus","blur"],o=4,a=1e3,c=2e3,d=["PageAction","UserAction","BrowserPerformance"],u={RESOURCES:"experimental.resources",REGISTER:"register"}},3434:(e,t,r)=>{"use strict";r.d(t,{Jt:()=>o,YM:()=>u});var n=r(7836),i=r(5607),s=r(5732);const o="nr@original:".concat(i.W),a=50;var c=Object.prototype.hasOwnProperty,d=!1;function u(e,t,r){return e||(e=n.ee),i.inPlace=function(e,t,r,n,s,o){r||(r="");const a="-"===r.charAt(0);for(let c=0;c<t.length;c++){const d=t[c],u=e[d];f(u)||(e[d]=i(u,a?d+r:r,n,d,s,o))}},i.flag=o,i;function i(t,n,i,d,h,p){return f(t)?t:(n||(n=""),nrWrapper[o]=t,function(e,t,r){if(Object.defineProperty&&Object.keys)try{return Object.keys(e).forEach(function(r){Object.defineProperty(t,r,{get:function(){return e[r]},set:function(t){return e[r]=t,t}})}),t}catch(e){l([e],r)}for(var n in e)c.call(e,n)&&(t[n]=e[n])}(t,nrWrapper,e),nrWrapper);function nrWrapper(){var o,c,f,g;let m,v;try{c=this,o=[...arguments],v=p?(0,s.$5)(r):[void 0],f="function"==typeof i?i(o,c):i||{}}catch(t){l([t,"",[o,c,d],f],e)}u(n+"start",[o,c,d,v],f,h);const y=performance.now();let b;try{return g=t.apply(c,o),b=performance.now(),g}catch(e){throw b=performance.now(),u(n+"err",[o,c,e,v],f,h),m=e,m}finally{const e=b-y,t={start:y,end:b,duration:e,isLongTask:e>=a,methodName:d,thrownError:m};t.isLongTask&&u("long-task",[t,c,v],f,h),u(n+"end",[o,c,g,v],f,h)}}}function u(r,n,i,s){if(!d||t){var o=d;d=!0;try{e.emit(r,n,i,t,s)}catch(t){l([t,r,n,i],e)}d=o}}}function l(e,t){t||(t=n.ee);try{t.emit("internal-error",e)}catch(e){}}function f(e){return!(e&&"function"==typeof e&&e.apply&&!e[o])}},3606:(e,t,r)=>{"use strict";r.d(t,{i:()=>s});var n=r(9908);s.on=o;var i=s.handlers={};function s(e,t,r,s){o(s||n.d,i,e,t,r)}function o(e,t,r,i,s){s||(s="feature"),e||(e=n.d);var o=t[s]=t[s]||{};(o[r]=o[r]||[]).push([e,i])}},3738:(e,t,r)=>{"use strict";r.d(t,{He:()=>i,Kp:()=>a,Lc:()=>d,Rz:()=>u,TZ:()=>n,bD:()=>s,d3:()=>o,jx:()=>l,sl:()=>f,uP:()=>c});const n=r(860).K7.sessionTrace,i="bstResource",s="resource",o="-start",a="-end",c="fn"+o,d="fn"+a,u="pushState",l=1e3,f=3e4},3785:(e,t,r)=>{"use strict";r.d(t,{R:()=>c,b:()=>d});var n=r(9908),i=r(1863),s=r(860),o=r(3969),a=r(993);function c(e,t,r={},c=a.p\_.INFO,d=!0,u,l=(0,i.t)()){(0,n.p)(o.xV,["API/logging/".concat(c.toLowerCase(),"/called")],void 0,s.K7.metrics,e),(0,n.p)(a.ET,[l,t,r,c,d,u],void 0,s.K7.logging,e)}function d(e){return"string"==typeof e&&Object.values(a.p\_).some(t=>t===e.toUpperCase().trim())}},3878:(e,t,r)=>{"use strict";function n(e,t){return{capture:e,passive:!1,signal:t}}function i(e,t,r=!1,i){window.addEventListener(e,t,n(r,i))}function s(e,t,r=!1,i){document.addEventListener(e,t,n(r,i))}r.d(t,{DD:()=>s,jT:()=>n,sp:()=>i})},3962:(e,t,r)=>{"use strict";r.d(t,{AM:()=>o,O2:()=>l,OV:()=>s,Qu:()=>f,TZ:()=>c,ih:()=>h,pP:()=>a,t1:()=>u,tC:()=>i,wD:()=>d});var n=r(860);const i=["click","keydown","submit"],s="popstate",o="api",a="initialPageLoad",c=n.K7.softNav,d=5e3,u=500,l={INITIAL\_PAGE\_LOAD:"",ROUTE\_CHANGE:1,UNSPECIFIED:2},f={INTERACTION:1,AJAX:2,CUSTOM\_END:3,CUSTOM\_TRACER:4},h={IP:"in progress",PF:"pending finish",FIN:"finished",CAN:"cancelled"}},3969:(e,t,r)=>{"use strict";r.d(t,{TZ:()=>n,XG:()=>a,rs:()=>i,xV:()=>o,z\_:()=>s});const n=r(860).K7.metrics,i="sm",s="cm",o="storeSupportabilityMetrics",a="storeEventMetrics"},4234:(e,t,r)=>{"use strict";r.d(t,{W:()=>i});var n=r(1687);class i{constructor(e,t){this.agentRef=e,this.ee=e?.ee,this.featureName=t,this.blocked=!1}deregisterDrain(){(0,n.x3)(this.agentRef,this.featureName)}}},4261:(e,t,r)=>{"use strict";r.d(t,{$9:()=>u,BL:()=>c,CH:()=>p,Dl:()=>R,Fw:()=>w,PA:()=>v,Pl:()=>n,Pv:()=>x,Tb:()=>f,U2:()=>o,V1:()=>A,Wb:()=>T,bt:()=>b,cD:()=>y,d3:()=>E,dT:()=>d,eY:()=>g,fF:()=>h,hG:()=>s,hw:()=>i,k6:()=>a,nb:()=>m,o5:()=>l});const n="api-",i=n+"ixn-",s="addPageAction",o="addToTrace",a="addRelease",c="finished",d="interaction",u="log",l="noticeError",f="pauseReplay",h="recordCustomEvent",p="recordReplay",g="register",m="setApplicationVersion",v="setCurrentRouteName",y="setCustomAttribute",b="setErrorHandler",w="setPageViewName",R="setUserId",E="start",T="wrapLogger",A="measure",x="consent"},5205:(e,t,r)=>{"use strict";r.d(t,{j:()=>x});var n=r(384),i=r(1741);var s=r(2555),o=r(3333);const a=e=>{if(!e||"string"!=typeof e)return!1;try{document.createDocumentFragment().querySelector(e)}catch{return!1}return!0};var c=r(2614),d=r(944),u=r(8122);const l="[data-nr-mask]",f=e=>(0,u.a)(e,(()=>{const e={feature\_flags:[],experimental:{register:!1,resources:!1},mask\_selector:"\*",block\_selector:"[data-nr-block]",mask\_input\_options:{color:!1,date:!1,"datetime-local":!1,email:!1,month:!1,number:!1,range:!1,search:!1,tel:!1,text:!1,time:!1,url:!1,week:!1,textarea:!1,select:!1,password:!0}};return{ajax:{deny\_list:void 0,block\_internal:!0,enabled:!0,autoStart:!0},api:{register:{get enabled(){return e.feature\_flags.includes(o.$v.REGISTER)||e.experimental.register},set enabled(t){e.experimental.register=t},duplicate\_data\_to\_container:!1}},browser\_consent\_mode:{enabled:!1},distributed\_tracing:{enabled:void 0,exclude\_newrelic\_header:void 0,cors\_use\_newrelic\_header:void 0,cors\_use\_tracecontext\_headers:void 0,allowed\_origins:void 0},get feature\_flags(){return e.feature\_flags},set feature\_flags(t){e.feature\_flags=t},generic\_events:{enabled:!0,autoStart:!0},harvest:{interval:30},jserrors:{enabled:!0,autoStart:!0},logging:{enabled:!0,autoStart:!0},metrics:{enabled:!0,autoStart:!0},obfuscate:void 0,page\_action:{enabled:!0},page\_view\_event:{enabled:!0,autoStart:!0},page\_view\_timing:{enabled:!0,autoStart:!0},performance:{capture\_marks:!1,capture\_measures:!1,capture\_detail:!0,resources:{get enabled(){return e.feature\_flags.includes(o.$v.RESOURCES)||e.experimental.resources},set enabled(t){e.experimental.resources=t},asset\_types:[],first\_party\_domains:[],ignore\_newrelic:!0}},privacy:{cookies\_enabled:!0},proxy:{assets:void 0,beacon:void 0},session:{expiresMs:c.wk,inactiveMs:c.BB},session\_replay:{autoStart:!0,enabled:!1,preload:!1,sampling\_rate:10,error\_sampling\_rate:100,collect\_fonts:!1,inline\_images:!1,fix\_stylesheets:!0,mask\_all\_inputs:!0,get mask\_text\_selector(){return e.mask\_selector},set mask\_text\_selector(t){a(t)?e.mask\_selector="".concat(t,",").concat(l):""===t||null===t?e.mask\_selector=l:(0,d.R)(5,t)},get block\_class(){return"nr-block"},get ignore\_class(){return"nr-ignore"},get mask\_text\_class(){return"nr-mask"},get block\_selector(){return e.block\_selector},set block\_selector(t){a(t)?e.block\_selector+=",".concat(t):""!==t&&(0,d.R)(6,t)},get mask\_input\_options(){return e.mask\_input\_options},set mask\_input\_options(t){t&&"object"==typeof t?e.mask\_input\_options={...t,password:!0}:(0,d.R)(7,t)}},session\_trace:{enabled:!0,autoStart:!0},soft\_navigations:{enabled:!0,autoStart:!0},ssl:void 0,user\_actions:{enabled:!0,elementAttributes:["id","className","tagName","type"]}}})());var h=r(6154),p=r(9324);let g=0;const m={buildEnv:p.F3,distMethod:p.Xs,version:p.xv,originTime:h.WN},v={consented:!1},y={activatedFeatures:void 0,appMetadata:{},configured:!1,get consented(){return this.session?.state?.consent||v.consented},set consented(e){v.consented=e},customTransaction:void 0,denyList:[],disabled:!1,drainRegistry:new Map,harvester:void 0,isolatedBacklog:!1,isRecording:!1,loaderType:void 0,maxBytes:3e4,obfuscator:void 0,onerror:void 0,ptid:void 0,releaseIds:{},session:void 0,timeKeeper:void 0,registeredEntities:[],jsAttributesMetadata:{bytes:0},get harvestCount(){return++g}},b=e=>{const t=(0,u.a)(e,y),r=Object.keys(m).reduce((e,t)=>(e[t]={value:m[t],writable:!1,configurable:!0,enumerable:!0},e),{});return Object.defineProperties(t,r)},w=e=>{const t=e.startsWith("http");e+="/",r.p=t?e:"https://"+e};var R=r(7836),E=r(3241);const T={accountID:void 0,trustKey:void 0,agentID:void 0,licenseKey:void 0,applicationID:void 0,xpid:void 0},A=e=>(0,u.a)(e,T);function x(e,t={},r,o){let{init:a,info:c,loader\_config:d,runtime:u={},exposed:l=!0}=t;if(!c){const e=(0,n.pV)();a=e.init,c=e.info,d=e.loader\_config}e.init=f(a||{}),e.loader\_config=A(d||{}),c.jsAttributes??={},h.bv&&(c.jsAttributes.isWorker=!0),e.info=(0,s.D)(c);const p=e.init;e.runtime??=b(u),p.proxy.assets&&w(p.proxy.assets),e.runtime.configured||(Object.defineProperty(e,"beacons",{get:()=>[e.info.beacon,e.info.errorBeacon,e.init.proxy.assets,e.init.proxy.beacon].filter(Boolean)}),Object.defineProperty(e.runtime,"denyList",{get:()=>[...e.init.ajax.deny\_list||[],...e.init.ajax.block\_internal?e.beacons:[]]}),e.runtime.ptid=e.agentIdentifier,function(e){const t=(0,n.pV)();Object.getOwnPropertyNames(i.W.prototype).forEach(r=>{const n=i.W.prototype[r];if("function"!=typeof n||"constructor"===n)return;let s=t[r];e[r]&&!1!==e.exposed&&"micro-agent"!==e.runtime?.loaderType&&(t[r]=(...t)=>{const n=e[r](...t);return s?s(...t):n})})}(e),e.runtime.loaderType=r,e.ee=R.ee.get(e.agentIdentifier),e.exposed=l,(0,E.W)({drained:!!e.runtime.activatedFeatures,type:"lifecycle",name:"initialize",feature:void 0,data:e.config}),e.runtime.configured=!0)}},5270:(e,t,r)=>{"use strict";r.d(t,{Aw:()=>o,SR:()=>s,rF:()=>a});var n=r(384),i=r(7767);function s(e){return!!(0,n.dV)().o.MO&&(0,i.V)(e)&&!0===e?.session\_trace.enabled}function o(e){return!0===e?.session\_replay.preload&&s(e)}function a(e,t){try{if("string"==typeof t?.type){if("password"===t.type.toLowerCase())return"\*".repeat(e?.length||0);if(void 0!==t?.dataset?.nrUnmask||t?.classList?.contains("nr-unmask"))return e}}catch(e){}return"string"==typeof e?e.replace(/[\S]/g,"\*"):"\*".repeat(e?.length||0)}},5289:(e,t,r)=>{"use strict";r.d(t,{GG:()=>o,Qr:()=>c,sB:()=>a});var n=r(3878),i=r(6389);function s(){return"undefined"==typeof document||"complete"===document.readyState}function o(e,t){if(s())return e();const r=(0,i.J)(e),o=setInterval(()=>{s()&&(clearInterval(o),r())},500);(0,n.sp)("load",r,t)}function a(e){if(s())return e();(0,n.DD)("DOMContentLoaded",e)}function c(e){if(s())return e();(0,n.sp)("popstate",e)}},5607:(e,t,r)=>{"use strict";r.d(t,{W:()=>n});const n=(0,r(9566).bz)()},5732:(e,t,r)=>{"use strict";r.d(t,{$5:()=>u,B5:()=>d,Ms:()=>s,Ux:()=>a,YA:()=>c,fQ:()=>i,yx:()=>o});var n=r(7508);const i={MFE:"MFE",BA:"BA"};function s(e,t){if(!e||!t?.init.api.register.enabled)return[];const r=t.runtime.registeredEntities;return r?.filter(t=>String(t.metadata.target.id)===String(e)).map(e=>e.metadata.target)||[]}function o(e,t){if(!e||!t?.init.api.register.enabled)return[];const r=t.runtime.registeredEntities;return r?.filter(t=>t.metadata.timings?.asset?.endsWith(e)).map(e=>e.metadata.target)||[]}function a(e,t){if(!l(t))return{};const r=t.agentRef.runtime.appMetadata.agents[0].entityGuid;return e?e.attributes:{"entity.guid":r,appId:t.agentRef.info.applicationID}}function c(e,t){return d(e,t)?{"child.id":e.id,"child.type":e.type,...a(void 0,t)}:{}}function d(e,t){return!!e&&!!l(t)&&t.agentRef.init.api.register.duplicate\_data\_to\_container}function u(e){if(!e?.init.api.register.enabled)return[void 0];const t=[];try{var r=(0,n.AZ)((0,n.QL)());let i=r.length-1;for(;r[i];)t.push(...o(r[i--],e))}catch(e){}return t.length||t.push(void 0),t}function l(e){return 2===e?.harvestEndpointVersion}},6154:(e,t,r)=>{"use strict";r.d(t,{OF:()=>d,RI:()=>i,WN:()=>f,bv:()=>s,gm:()=>o,lR:()=>l,m:()=>c,mw:()=>a,sb:()=>u,zk:()=>h});var n=r(1863);const i="undefined"!=typeof window&&!!window.document,s="undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self.navigator instanceof WorkerNavigator||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis.navigator instanceof WorkerNavigator),o=i?window:"undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis),a=Boolean("hidden"===o?.document?.visibilityState),c=""+o?.location,d=/iPad|iPhone|iPod/.test(o.navigator?.userAgent),u=d&&"undefined"==typeof SharedWorker,l=(()=>{const e=o.navigator?.userAgent?.match(/Firefox[/\s](\d+\.\d+)/);return Array.isArray(e)&&e.length>=2?+e[1]:0})(),f=Date.now()-(0,n.t)(),h=()=>{const e=o?.performance?.getEntriesByType?.("navigation")?.[0];if(e&&e.responseStart>0&&e.responseStart<o.performance.now())return e}},6344:(e,t,r)=>{"use strict";r.d(t,{BB:()=>u,Qb:()=>l,TZ:()=>i,Ug:()=>o,Vh:()=>s,\_s:()=>a,bc:()=>d,yP:()=>c});var n=r(2614);const i=r(860).K7.sessionReplay,s="errorDuringReplay",o=.12,a={DomContentLoaded:0,Load:1,FullSnapshot:2,IncrementalSnapshot:3,Meta:4,Custom:5},c={[n.g.ERROR]:15e3,[n.g.FULL]:3e5,[n.g.OFF]:0},d={RESET:{message:"Session was reset",sm:"Reset"},IMPORT:{message:"Recorder failed to import",sm:"Import"},TOO\_MANY:{message:"429: Too Many Requests",sm:"Too-Many"},TOO\_BIG:{message:"Payload was too large",sm:"Too-Big"},CROSS\_TAB:{message:"Session Entity was set to OFF on another tab",sm:"Cross-Tab"},ENTITLEMENTS:{message:"Session Replay is not allowed and will not be started",sm:"Entitlement"}},u=5e3,l={API:"api",RESUME:"resume",SWITCH\_TO\_FULL:"switchToFull",INITIALIZE:"initialize",PRELOAD:"preload"}},6389:(e,t,r)=>{"use strict";function n(e,t=500,r={}){const n=r?.leading||!1;let i;return(...r)=>{n&&void 0===i&&(e.apply(this,r),i=setTimeout(()=>{i=clearTimeout(i)},t)),n||(clearTimeout(i),i=setTimeout(()=>{e.apply(this,r)},t))}}function i(e){let t=!1;return(...r)=>{t||(t=!0,e.apply(this,r))}}r.d(t,{J:()=>i,s:()=>n})},6630:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.pageViewEvent},6774:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.jserrors},7295:(e,t,r)=>{"use strict";r.d(t,{Xv:()=>o,gX:()=>i,iW:()=>s});var n=[];function i(e){if(!e||s(e))return!1;if(0===n.length)return!0;if("\*"===n[0].hostname)return!1;for(var t=0;t<n.length;t++){var r=n[t];if(r.hostname.test(e.hostname)&&r.pathname.test(e.pathname))return!1}return!0}function s(e){return void 0===e.hostname}function o(e){if(n=[],e&&e.length)for(var t=0;t<e.length;t++){let r=e[t];if(!r)continue;if("\*"===r)return void(n=[{hostname:"\*"}]);0===r.indexOf("http://")?r=r.substring(7):0===r.indexOf("https://")&&(r=r.substring(8));const i=r.indexOf("/");let s,o;i>0?(s=r.substring(0,i),o=r.substring(i)):(s=r,o="\*");let[c]=s.split(":");n.push({hostname:a(c),pathname:a(o,!0)})}}function a(e,t=!1){const r=e.replace(/[.+?^${}()|[\]\\]/g,e=>"\\"+e).replace(/\\*/g,".\*?");return new RegExp((t?"^":"")+r+"$")}},7485:(e,t,r)=>{"use strict";r.d(t,{D:()=>i});var n=r(6154);function i(e){if(0===(e||"").indexOf("data:"))return{protocol:"data"};try{const t=new URL(e,location.href),r={port:t.port,hostname:t.hostname,pathname:t.pathname,search:t.search,protocol:t.protocol.slice(0,t.protocol.indexOf(":")),sameOrigin:t.protocol===n.gm?.location?.protocol&&t.host===n.gm?.location?.host};return r.port&&""!==r.port||("http:"===t.protocol&&(r.port="80"),"https:"===t.protocol&&(r.port="443")),r.pathname&&""!==r.pathname?r.pathname.startsWith("/")||(r.pathname="/".concat(r.pathname)):r.pathname="/",r}catch(e){return{}}}},7508:(e,t,r)=>{"use strict";r.d(t,{AZ:()=>g,Qr:()=>b,QL:()=>m});var n=r(6154),i=r(1863),s=r(9119),o=r(7866);class a{dom=new c;performance=new c;constructor(e){this.url=e}get script(){const e=Math.max(this.dom.start,this.performance.end);return{start:e,end:Math.max(this.dom.end,this.performance.end,e)}}}class c{start=0;end=0;value=void 0}let d;try{d=g(m())[0]}catch(e){d=g(e)[0]}const u=e=>"script"===e.initiatorType||["link","fetch"].includes(e.initiatorType)&&e.name.endsWith(".js"),l=new Map;let f=[];function h(e){return l.get(e)}function p(e){const t=h(e);if(t)return t;const r=new a(e);if(l.set(e,r),l.size>1e3){const e=l.keys().next().value;l.delete(e)}return r}if(n.gm.MutationObserver&&n.gm.document){new MutationObserver(e=>{e.forEach(e=>{e.addedNodes.forEach(e=>{if("SCRIPT"===e.nodeName&&e.src){const t=p((0,s.L)(e.src));t.dom.start=(0,i.t)(),t.dom.value=e;const r=()=>{t.dom.end=(0,i.t)()};["load","error"].forEach(t=>e.addEventListener(t,r,{once:!0}))}})})}).observe(n.gm.document,{childList:!0,subtree:!0})}if(n.gm.PerformanceObserver?.supportedEntryTypes.includes("resource")){new PerformanceObserver(e=>{e.getEntries().filter(u).forEach(e=>{const t=p((0,s.L)(e.name));t.performance.start=Math.floor(e.startTime),t.performance.end=Math.floor(e.responseEnd),t.performance.value=e;const r=[];f.forEach(({test:t,addedAt:n},s)=>{(t(e)||(0,i.t)()-n>1e4)&&r.push(s)}),f=f.filter((e,t)=>!r.includes(t))})}).observe({type:"resource",buffered:!0})}function g(e){if(!e||"string"!=typeof e)return[];const t=new Set,r=e.split("\n");for(const e of r){const r=e.match(o.cn)||e.match(o.hB)||e.match(o.fL);if(r&&r[2])t.add((0,s.L)(r[2]));else{const r=e.match(/\(([^)]+\.js):\d+:\d+\)/)||e.match(/^\s+at\s+([^\s(]+\.js):\d+:\d+/);r&&r[1]&&t.add((0,s.L)(r[1]))}}return[...t]}function m(){let e;try{const t=Error.stackTraceLimit;Error.stackTraceLimit=50,e=(new Error).stack,Error.stackTraceLimit=t}catch(t){e=(new Error).stack}return e}function v(e,t){return(0,s.L)(e.name)===t}function y(e,t){e.fetchStart=Math.floor(t.startTime),e.fetchEnd=Math.floor(t.responseEnd),e.asset=t.name,e.type=t.initiatorType}function b(){const e={registeredAt:(0,i.t)(),reportedAt:void 0,fetchStart:0,fetchEnd:0,scriptStart:0,scriptEnd:0,asset:void 0,type:"unknown"},t=m();if(!t)return e;const r=n.gm.performance?.getEntriesByType("navigation")?.[0]?.name||"";try{const o=g(t),a=(o.length>1?o.filter(e=>d!==e):o)[0];if(!a)return e;if(r.includes(a))return e.asset=(0,s.L)(r),e.type="inline",e;e.correlation=h(a);const c=e.correlation?.performance.value||performance.getEntriesByType("resource").find(e=>v(e,a));c?y(e,c):function(e){if(!e||!n.gm.document)return!1;try{const t=n.gm.document.querySelectorAll('link[rel="preload"][as="script"]');for(const r of t)if((0,s.L)(r.href)===e)return!0}catch(e){}return!1}(a)&&(e.asset=a,e.type="preload",f.push({addedAt:(0,i.t)(),test:t=>!!v(t,a)&&(y(e,t),!0)})),Object.defineProperty(e,"scriptStart",{get:()=>e.correlation?.script.start||e.fetchEnd}),Object.defineProperty(e,"scriptEnd",{get:()=>e.correlation?.script.end||e.registeredAt})}catch(e){}return e}},7699:(e,t,r)=>{"use strict";r.d(t,{It:()=>s,KC:()=>a,No:()=>i,qh:()=>o});var n=r(860);const i=16e3,s=1e6,o="SESSION\_ERROR",a={[n.K7.logging]:!0,[n.K7.genericEvents]:!0,[n.K7.jserrors]:!0,[n.K7.ajax]:!0}},7767:(e,t,r)=>{"use strict";r.d(t,{V:()=>i});var n=r(6154);const i=e=>n.RI&&!0===e?.privacy.cookies\_enabled},7836:(e,t,r)=>{"use strict";r.d(t,{P:()=>a,ee:()=>c});var n=r(384),i=r(8990),s=r(2646),o=r(5607);const a="nr@context:".concat(o.W),c=function e(t,r){var n={},o={},u={},l=!1;try{l=16===r.length&&d.initializedAgents?.[r]?.runtime.isolatedBacklog}catch(e){}var f={on:p,addEventListener:p,removeEventListener:function(e,t){var r=n[e];if(!r)return;for(var i=0;i<r.length;i++)r[i]===t&&r.splice(i,1)},emit:function(e,r,n,i,s){!1!==s&&(s=!0);if(c.aborted&&!i)return;t&&s&&t.emit(e,r,n);var a=h(n);g(e).forEach(e=>{e.apply(a,r)});var d=v()[o[e]];d&&d.push([f,e,r,a]);return a},get:m,listeners:g,context:h,buffer:function(e,t){const r=v();if(t=t||"feature",f.aborted)return;Object.entries(e||{}).forEach(([e,n])=>{o[n]=t,t in r||(r[t]=[])})},abort:function(){f.\_aborted=!0,Object.keys(f.backlog).forEach(e=>{delete f.backlog[e]})},isBuffering:function(e){return!!v()[o[e]]},debugId:r,backlog:l?{}:t&&"object"==typeof t.backlog?t.backlog:{},isolatedBacklog:l};return Object.defineProperty(f,"aborted",{get:()=>{let e=f.\_aborted||!1;return e||(t&&(e=t.aborted),e)}}),f;function h(e){return e&&e instanceof s.y?e:e?(0,i.I)(e,a,()=>new s.y(a)):new s.y(a)}function p(e,t){n[e]=g(e).concat(t)}function g(e){return n[e]||[]}function m(t){return u[t]=u[t]||e(f,t)}function v(){return f.backlog}}(void 0,"globalEE"),d=(0,n.Zm)();d.ee||(d.ee=c)},7866:(e,t,r)=>{"use strict";r.d(t,{Nc:()=>s,cn:()=>a,fL:()=>i,h3:()=>n,hB:()=>o});const n=/function (.+?)\s\*\(/,i=/^\s\*at .+ \(eval at \S+ \((?:(?:file|http|https):[^)]+)?\)(?:, [^:]\*:\d+:\d+)?\)$/i,s=/^\s\*at Function code \(Function code:\d+:\d+\)\s\*/i,o=/^\s\*at (?:((?:\[object object\])?(?:[^(]\*\([^)]\*\))\*[^()]\*(?: \[as \S+\])?) )?\(?((?:file|http|https|chrome-extension):.\*?)?:(\d+)(?::(\d+))?\)?\s\*$/i,a=/^\s\*(?:([^@]\*)(?:\(.\*?\))?@)?((?:file|http|https|chrome|safari-extension).\*?):(\d+)(?::(\d+))?\s\*$/i},8122:(e,t,r)=>{"use strict";r.d(t,{a:()=>i});var n=r(944);function i(e,t){try{if(!e||"object"!=typeof e)return(0,n.R)(3);if(!t||"object"!=typeof t)return(0,n.R)(4);const r=Object.create(Object.getPrototypeOf(t),Object.getOwnPropertyDescriptors(t)),s=0===Object.keys(r).length?e:r;for(let o in s)if(void 0!==e[o])try{if(null===e[o]){r[o]=null;continue}Array.isArray(e[o])&&Array.isArray(t[o])?r[o]=Array.from(new Set([...e[o],...t[o]])):e[o]instanceof Map||e[o]instanceof Set||e[o]instanceof Date||e[o]instanceof RegExp?r[o]=e[o]:"object"==typeof e[o]&&"object"==typeof t[o]?r[o]=i(e[o],t[o]):r[o]=e[o]}catch(e){r[o]||(0,n.R)(1,e)}return r}catch(e){(0,n.R)(2,e)}}},8139:(e,t,r)=>{"use strict";r.d(t,{u:()=>f});var n=r(7836),i=r(3434),s=r(8990),o=r(6154);const a={},c=o.gm.XMLHttpRequest,d="addEventListener",u="removeEventListener",l="nr@wrapped:".concat(n.P);function f(e){var t=function(e){return(e||n.ee).get("events")}(e);if(a[t.debugId]++)return t;a[t.debugId]=1;var r=(0,i.YM)(t,!0);function f(e){r.inPlace(e,[d,u],"-",p)}function p(e,t){return e[1]}return"getPrototypeOf"in Object&&(o.RI&&h(document,f),c&&h(c.prototype,f),h(o.gm,f)),t.on(d+"-start",function(e,t){var n=e[1];if(null!==n&&("function"==typeof n||"object"==typeof n)&&"newrelic"!==e[0]){var i=(0,s.I)(n,l,function(){var e={object:function(){if("function"!=typeof n.handleEvent)return;return n.handleEvent.apply(n,arguments)},function:n}[typeof n];return e?r(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=e[1]=i}}),t.on(u+"-start",function(e){e[1]=this.wrapped||e[1]}),t}function h(e,t,...r){let n=e;for(;"object"==typeof n&&!Object.prototype.hasOwnProperty.call(n,d);)n=Object.getPrototypeOf(n);n&&t(n,...r)}},8362:(e,t,r)=>{"use strict";r.d(t,{d:()=>s});var n=r(9566),i=r(1741);class s extends i.W{agentIdentifier=(0,n.LA)(16)}},8374:(e,t,r)=>{r.nc=(()=>{try{return document?.currentScript?.nonce}catch(e){}return""})()},8990:(e,t,r)=>{"use strict";r.d(t,{I:()=>i});var n=Object.prototype.hasOwnProperty;function i(e,t,r){if(n.call(e,t))return e[t];var i=r();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:i,writable:!0,enumerable:!1}),i}catch(e){}return e[t]=i,i}},9119:(e,t,r)=>{"use strict";r.d(t,{L:()=>s});var n=/([^?#]\*)[^#]\*(#[^?]\*|$).\*/,i=/([^?#]\*)().\*/;function s(e,t){return e?e.replace(t?n:i,"$1$2"):e}},9300:(e,t,r)=>{"use strict";r.d(t,{T:()=>n,f:()=>i});const n=r(860).K7.ajax,i="ajaxRequest.id"},9324:(e,t,r)=>{"use strict";r.d(t,{AJ:()=>o,F3:()=>i,Xs:()=>s,Yq:()=>a,xv:()=>n});const n="1.314.0",i="PROD",s="CDN",o="@newrelic/rrweb",a="1.1.0"},9566:(e,t,r)=>{"use strict";r.d(t,{LA:()=>a,ZF:()=>c,bz:()=>o,el:()=>d});var n=r(6154);const i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx";function s(e,t){return e?15&e[t]:16\*Math.random()|0}function o(){const e=n.gm?.crypto||n.gm?.msCrypto;let t,r=0;return e&&e.getRandomValues&&(t=e.getRandomValues(new Uint8Array(30))),i.split("").map(e=>"x"===e?s(t,r++).toString(16):"y"===e?(3&s()|8).toString(16):e).join("")}function a(e){const t=n.gm?.crypto||n.gm?.msCrypto;let r,i=0;t&&t.getRandomValues&&(r=t.getRandomValues(new Uint8Array(e)));const o=[];for(var a=0;a<e;a++)o.push(s(r,i++).toString(16));return o.join("")}function c(){return a(16)}function d(){return a(32)}},9908:(e,t,r)=>{"use strict";r.d(t,{d:()=>n,p:()=>i});var n=r(7836).ee.get("handle");function i(e,t,r,i,s){s?(s.buffer([e],i),s.emit(e,t,r)):(n.buffer([e],i),n.emit(e,t,r))}}},n={};function i(e){var t=n[e];if(void 0!==t)return t.exports;var s=n[e]={exports:{}};return r[e](s,s.exports,i),s.exports}i.m=r,i.d=(e,t)=>{for(var r in t)i.o(t,r)&&!i.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},i.f={},i.e=e=>Promise.all(Object.keys(i.f).reduce((t,r)=>(i.f[r](e,t),t),[])),i.u=e=>({212:"nr-spa-compressor",249:"nr-spa-recorder",478:"nr-spa"}[e]+"-1.314.0.min.js"),i.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),e={},t="NRBA-1.314.0.PROD:",i.l=(r,n,s,o)=>{if(e[r])e[r].push(n);else{var a,c;if(void 0!==s)for(var d=document.getElementsByTagName("script"),u=0;u<d.length;u++){var l=d[u];if(l.getAttribute("src")==r||l.getAttribute("data-webpack")==t+s){a=l;break}}if(!a){c=!0;var f={478:"sha512-mgj9qD5BdNJpEJCPmd1OfPzfnL/HRJ64OPYq/GZQxKc0756ytnQixcg8IA8iZWe/PRWN4DuGAnX82J2lscbiIw==",249:"sha512-fUJXIKjSt6UL9n1UZzNMzGGL3CxnBT/AgtoTat0/ONINbEB2PoiO+yK54DPYDwzpXDBddJHvs2BrYFj1GBpo2Q==",212:"sha512-vjoeBTgR0ONx6WcgBdfuPgcta1834zMPDhLL05C9c/pB+/xAuxL4BJMu9yeXYh+oIV7oIn6qTkDC7rBcZIDiHg=="};(a=document.createElement("script")).charset="utf-8",i.nc&&a.setAttribute("nonce",i.nc),a.setAttribute("data-webpack",t+s),a.src=r,0!==a.src.indexOf(window.location.origin+"/")&&(a.crossOrigin="anonymous"),f[o]&&(a.integrity=f[o])}e[r]=[n];var h=(t,n)=>{a.onerror=a.onload=null,clearTimeout(p);var i=e[r];if(delete e[r],a.parentNode&&a.parentNode.removeChild(a),i&&i.forEach(e=>e(n)),t)return t(n)},p=setTimeout(h.bind(null,void 0,{type:"timeout",target:a}),12e4);a.onerror=h.bind(null,a.onerror),a.onload=h.bind(null,a.onload),c&&document.head.appendChild(a)}},i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"\_\_esModule",{value:!0})},i.p="https://js-agent.newrelic.com/",(()=>{var e={38:0,788:0};i.f.j=(t,r)=>{var n=i.o(e,t)?e[t]:void 0;if(0!==n)if(n)r.push(n[2]);else{var s=new Promise((r,i)=>n=e[t]=[r,i]);r.push(n[2]=s);var o=i.p+i.u(t),a=new Error;i.l(o,r=>{if(i.o(e,t)&&(0!==(n=e[t])&&(e[t]=void 0),n)){var s=r&&("load"===r.type?"missing":r.type),o=r&&r.target&&r.target.src;a.message="Loading chunk "+t+" failed: ("+s+": "+o+")",a.name="ChunkLoadError",a.type=s,a.request=o,n[1](a)}},"chunk-"+t,t)}};var t=(t,r)=>{var n,s,[o,a,c]=r,d=0;if(o.some(t=>0!==e[t])){for(n in a)i.o(a,n)&&(i.m[n]=a[n]);if(c)c(i)}for(t&&t(r);d<o.length;d++)s=o[d],i.o(e,s)&&e[s]&&e[s][0](),e[s]=0},r=self["webpackChunk:NRBA-1.314.0.PROD"]=self["webpackChunk:NRBA-1.314.0.PROD"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})(),(()=>{"use strict";i(8374);var e=i(8362),t=i(860);const r=Object.values(t.K7);var n=i(5205);var s=i(9908),o=i(1863),a=i(4261),c=i(1738);var d=i(1687),u=i(4234),l=i(5289),f=i(6154),h=i(944),p=i(5270),g=i(7767),m=i(6389),v=i(7699);class y extends u.W{constructor(e,t){super(e,t),this.abortHandler=void 0,this.featAggregate=void 0,this.loadedSuccessfully=void 0,this.onAggregateImported=new Promise(e=>{this.loadedSuccessfully=e}),this.deferred=Promise.resolve(),!1===e.init[this.featureName].autoStart?this.deferred=new Promise((t,r)=>{this.ee.on("manual-start-all",(0,m.J)(()=>{(0,d.Ak)(e,this.featureName),t()}))}):(0,d.Ak)(e,t)}importAggregator(e,t,r={}){if(this.featAggregate)return;const n=async()=>{let n;await this.deferred;try{if((0,g.V)(e.init)){const{setupAgentSession:t}=await i.e(478).then(i.bind(i,8766));n=t(e)}}catch(e){(0,h.R)(20,e),this.ee.emit("internal-error",[e]),(0,s.p)(v.qh,[e],void 0,this.featureName,this.ee)}try{if(!this.#t(this.featureName,n,e.init))return(0,d.Ze)(this.agentRef,this.featureName),void this.loadedSuccessfully(!1);const{Aggregate:i}=await t();this.featAggregate=new i(e,r),e.runtime.harvester.initializedAggregates.push(this.featAggregate),this.loadedSuccessfully(!0)}catch(e){(0,h.R)(34,e),this.abortHandler?.(),(0,d.Ze)(this.agentRef,this.featureName,!0),this.loadedSuccessfully(!1),this.ee&&this.ee.abort()}};f.RI?(0,l.GG)(()=>n(),!0):n()}#t(e,r,n){if(this.blocked)return!1;switch(e){case t.K7.sessionReplay:return(0,p.SR)(n)&&!!r;case t.K7.sessionTrace:return!!r;default:return!0}}}var b=i(6630),w=i(2614),R=i(3241);class E extends y{static featureName=b.T;constructor(e){var t;super(e,b.T),this.setupInspectionEvents(),t=e,(0,c.Y)(a.Fw,function(e,r){"string"==typeof e&&("/"!==e.charAt(0)&&(e="/"+e),t.runtime.customTransaction=(r||"http://custom.transaction")+e,(0,s.p)(a.Pl+a.Fw,[(0,o.t)()],void 0,void 0,t.ee))},t),this.importAggregator(e,()=>i.e(478).then(i.bind(i,5839)))}setupInspectionEvents(){const e=(e,t)=>{e&&(0,R.W)({timeStamp:e.timeStamp,loaded:"complete"===e.target.readyState,type:"window",name:t,data:e.target.location+""})};(0,l.sB)(t=>{e(t,"DOMContentLoaded")}),(0,l.GG)(t=>{e(t,"load")}),(0,l.Qr)(t=>{e(t,"navigate")}),this.ee.on(w.tS.UPDATE,(e,t)=>{(0,R.W)({type:"lifecycle",name:"session",data:t})})}}var T=i(384);class A extends e.d{constructor(e){var t;(super(),f.gm)?(this.features={},(0,T.bQ)(this.agentIdentifier,this),this.desiredFeatures=new Set(e.features||[]),this.desiredFeatures.add(E),(0,n.j)(this,e,e.loaderType||"agent"),t=this,(0,c.Y)(a.cD,function(e,r,n=!1){if("string"==typeof e){if(["string","number","boolean"].includes(typeof r)||null===r)return(0,c.U)(t,e,r,a.cD,n);(0,h.R)(40,typeof r)}else(0,h.R)(39,typeof e)},t),function(e){(0,c.Y)(a.Dl,function(t,r=!1){if("string"!=typeof t&&null!==t)return void(0,h.R)(41,typeof t);const n=e.info.jsAttributes["enduser.id"];r&&null!=n&&n!==t?(0,s.p)(a.Pl+"setUserIdAndResetSession",[t],void 0,"session",e.ee):(0,c.U)(e,"enduser.id",t,a.Dl,!0)},e)}(this),function(e){(0,c.Y)(a.nb,function(t){if("string"==typeof t||null===t)return(0,c.U)(e,"application.version",t,a.nb,!1);(0,h.R)(42,typeof t)},e)}(this),function(e){(0,c.Y)(a.d3,function(){e.ee.emit("manual-start-all")},e)}(this),function(e){(0,c.Y)(a.Pv,function(t=!0){if("boolean"==typeof t){if((0,s.p)(a.Pl+a.Pv,[t],void 0,"session",e.ee),e.runtime.consented=t,t){const t=e.features.page\_view\_event;t.onAggregateImported.then(e=>{const r=t.featAggregate;e&&!r.sentRum&&r.sendRum()})}}else(0,h.R)(65,typeof t)},e)}(this),this.run()):(0,h.R)(21)}get config(){return{info:this.info,init:this.init,loader\_config:this.loader\_config,runtime:this.runtime}}get api(){return this}run(){try{const e=function(e){const t={};return r.forEach(r=>{t[r]=!!e[r]?.enabled}),t}(this.init),n=[...this.desiredFeatures];n.sort((e,r)=>t.P3[e.featureName]-t.P3[r.featureName]),n.forEach(r=>{if(!e[r.featureName]&&r.featureName!==t.K7.pageViewEvent)return;const n=function(e){switch(e){case t.K7.ajax:return[t.K7.jserrors];case t.K7.sessionTrace:return[t.K7.ajax,t.K7.pageViewEvent];case t.K7.sessionReplay:return[t.K7.sessionTrace];case t.K7.pageViewTiming:return[t.K7.pageViewEvent];default:return[]}}(r.featureName).filter(e=>!(e in this.features));n.length>0&&(0,h.R)(36,{targetFeature:r.featureName,missingDependencies:n}),this.features[r.featureName]=new r(this)})}catch(e){(0,h.R)(22,e);for(const e in this.features)this.features[e].abortHandler?.();const t=(0,T.Zm)();delete t.initializedAgents[this.agentIdentifier]?.features,delete this.sharedAggregator;return t.ee.get(this.agentIdentifier).abort(),!1}}}var x=i(2843),S=i(782);class \_ extends y{static featureName=S.T;constructor(e){super(e,S.T),f.RI&&((0,x.u)(()=>(0,s.p)("docHidden",[(0,o.t)()],void 0,S.T,this.ee),!0),(0,x.G)(()=>(0,s.p)("winPagehide",[(0,o.t)()],void 0,S.T,this.ee)),this.importAggregator(e,()=>i.e(478).then(i.bind(i,9917))))}}var O=i(3969);class P extends y{static featureName=O.TZ;constructor(e){super(e,O.TZ),this.importAggregator(e,()=>i.e(478).then(i.bind(i,6555)))}}var k=i(6774),N=i(3878),j=i(3304);class D{constructor(e,t,r,n,i){this.name="UncaughtError",this.message="string"==typeof e?e:(0,j.A)(e),this.sourceURL=t,this.line=r,this.column=n,this.\_\_newrelic=i}}function C(e){return M(e)?e:new D(void 0!==e?.message?e.message:e,e?.filename||e?.sourceURL,e?.lineno||e?.line,e?.colno||e?.col,e?.\_\_newrelic,e?.cause)}function L(e){const t="Unhandled Promise Rejection: ";if(!e?.reason)return;if(M(e.reason)){try{e.reason.message.startsWith(t)||(e.reason.message=t+e.reason.message)}catch(e){}return C(e.reason)}const r=C(e.reason);return(r.message||"").startsWith(t)||(r.message=t+r.message),r}function I(e){if(e.error instanceof SyntaxError&&!/:\d+$/.test(e.error.stack?.trim())){const t=new D(e.message,e.filename,e.lineno,e.colno,e.error.\_\_newrelic,e.cause);return t.name=SyntaxError.name,t}return M(e.error)?e.error:C(e)}function M(e){return e instanceof Error&&!!e.stack}function B(e,r,n,i,a=(0,o.t)()){"string"==typeof e&&(e=new Error(e)),(0,s.p)("err",[e,a,!1,r,n.runtime.isRecording,void 0,i],void 0,t.K7.jserrors,n.ee),(0,s.p)("uaErr",[],void 0,t.K7.genericEvents,n.ee)}var H=i(5732),K=i(993),W=i(3785);function F(e,{customAttributes:t={},level:r=K.p\_.INFO}={},n,i,s=(0,o.t)()){(0,W.R)(n.ee,e,t,r,!1,i,s)}function U(e,r,n,i,c=(0,o.t)()){(0,s.p)(a.Pl+a.hG,[c,e,r,i],void 0,t.K7.genericEvents,n.ee)}function V(e,r,n,i,c=(0,o.t)()){const{start:d,end:u,customAttributes:l}=r||{},f={customAttributes:l||{}};if("object"!=typeof f.customAttributes||"string"!=typeof e||0===e.length)return void(0,h.R)(57);const p=(e,t)=>null==e?t:"number"==typeof e?e:e instanceof PerformanceMark?e.startTime:Number.NaN;if(f.start=p(d,0),f.end=p(u,c),Number.isNaN(f.start)||Number.isNaN(f.end))(0,h.R)(57);else{if(f.duration=f.end-f.start,!(f.duration<0))return(0,s.p)(a.Pl+a.V1,[f,e,i],void 0,t.K7.genericEvents,n.ee),f;(0,h.R)(58)}}function z(e,r={},n,i,c=(0,o.t)()){(0,s.p)(a.Pl+a.fF,[c,e,r,i],void 0,t.K7.genericEvents,n.ee)}var G=i(7508),Y=i(9566);const Z=["name","id","type"],q=new Map([[U,"addPageAction"],[F,"log"],[V,"measure"],[B,"noticeError"],[z,"recordCustomEvent"]]),X={experimental:(0,m.J)(()=>(0,h.R)(54,"newrelic.register")),disabled:(0,m.J)(()=>(0,h.R)(55)),invalidTarget:(0,m.J)(e=>(0,h.R)(48,e)),deregistered:(0,m.J)(()=>(0,h.R)(68))};function Q(e){(0,c.Y)(a.eY,function(t){return J(e,t)},e)}function J(e,r){X.experimental(),r||={},r.instance=(0,Y.LA)(8),r.type=H.fQ.MFE,r.licenseKey||=e.info.licenseKey,r.blocked=!1,("object"!=typeof r.tags||null===r.tags||Array.isArray(r.tags))&&(r.tags={}),r.parent??={get id(){return e.runtime.appMetadata.agents[0].entityGuid},type:H.fQ.BA};const n=(0,G.Qr)(),i={};Object.prototype.hasOwnProperty.call(r,"attributes")||Object.defineProperty(r,"attributes",{get:()=>({...i,"source.id":r.id,"source.name":r.name,"source.type":r.type,"parent.type":r.parent?.type||H.fQ.BA,"parent.id":r.parent?.id})}),Object.entries(r.tags).forEach(([e,t])=>{Z.includes(e)||(i["source.".concat(e)]=t)});let a=()=>{};const c=e.runtime.registeredEntities,d=e=>{r.blocked=!0,a=e};function u(e){return"string"==typeof e&&!!e.trim()&&e.trim().length<501}e.init.api.register.enabled||d(X.disabled),u(r.id)&&u(r.name)||d(()=>X.invalidTarget(r));const l={addPageAction:(t,n={})=>m(U,[t,{...i,...n},e],r),deregister:()=>{p(),d(X.deregistered)},log:(t,n={})=>m(F,[t,{...n,customAttributes:{...i,...n.customAttributes||{}}},e],r),measure:(t,n={})=>m(V,[t,{...n,customAttributes:{...i,...n.customAttributes||{}}},e],r),noticeError:(t,n={})=>m(B,[t,{...i,...n},e],r),recordCustomEvent:(t,n={})=>m(z,[t,{...i,...n},e],r),setApplicationVersion:e=>g("application.version",e),setCustomAttribute:(e,t)=>g(e,t),setUserId:e=>g("enduser.id",e),metadata:{get customAttributes(){return i},target:r,timings:n}},f=()=>(r.blocked&&a(),r.blocked);function p(){if(n.reportedAt)return;n.reportedAt=(0,o.t)();const e=n.fetchEnd-n.fetchStart,t=n.scriptEnd-n.scriptStart;l.recordCustomEvent("MicroFrontEndTiming",{assetUrl:n.asset,assetType:n.type,timeAlive:n.reportedAt-n.registeredAt,timeToBeRequested:n.fetchStart,timeToExecute:t,timeToFetch:e,timeToLoad:e+t,timeToRegister:n.registeredAt})}f()||(c.push(l),(0,x.G)(p));const g=(e,t)=>{f()||(i[e]=t)},m=(r,n,i)=>{if(f()&&r!==J)return;const a=(0,o.t)(),c=q.get(r)||"unknown";(0,s.p)(O.xV,["API/register/".concat(c,"/called")],void 0,t.K7.metrics,e.ee);try{return r(...n,i,a)}catch(e){(0,h.R)(50,e)}};return l}class ee extends y{static featureName=k.T;constructor(e){var t;super(e,k.T),t=e,(0,c.Y)(a.o5,(e,r)=>B(e,r,t),t),function(e){(0,c.Y)(a.bt,function(t){e.runtime.onerror=t},e)}(e),function(e){let t=0;(0,c.Y)(a.k6,function(e,r){++t>10||(this.runtime.releaseIds[e.slice(-200)]=(""+r).slice(-200))},e)}(e),Q(e);try{this.removeOnAbort=new AbortController}catch(e){}this.ee.on("internal-error",(t,r)=>{this.abortHandler&&(0,s.p)("ierr",[C(t),(0,o.t)(),!0,{},e.runtime.isRecording,r],void 0,this.featureName,this.ee)}),f.gm.addEventListener("unhandledrejection",t=>{this.abortHandler&&(0,s.p)("err",[L(t),(0,o.t)(),!1,{unhandledPromiseRejection:1},e.runtime.isRecording],void 0,this.featureName,this.ee)},(0,N.jT)(!1,this.removeOnAbort?.signal)),f.gm.addEventListener("error",t=>{this.abortHandler&&(0,s.p)("err",[I(t),(0,o.t)(),!1,{},e.runtime.isRecording],void 0,this.featureName,this.ee)},(0,N.jT)(!1,this.removeOnAbort?.signal)),this.abortHandler=this.#r,this.importAggregator(e,()=>i.e(478).then(i.bind(i,9377)))}#r(){this.removeOnAbort?.abort(),this.abortHandler=void 0}}var te=i(8990);let re=1;function ne(e){const t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===f.gm?0:(0,te.I)(e,"nr@id",function(){return re++})}function ie(e){if("string"==typeof e&&e.length)return e.length;if("object"==typeof e){if("undefined"!=typeof ArrayBuffer&&e instanceof ArrayBuffer&&e.byteLength)return e.byteLength;if("undefined"!=typeof Blob&&e instanceof Blob&&e.size)return e.size;if(!("undefined"!=typeof FormData&&e instanceof FormData))try{return(0,j.A)(e).length}catch(e){return}}}var se=i(8139),oe=i(7836),ae=i(3434);const ce={},de=["open","send"];function ue(e,t){var r=e||oe.ee;const n=function(e){return(e||oe.ee).get("xhr")}(r);if(void 0===f.gm.XMLHttpRequest)return n;if(ce[n.debugId]++)return n;ce[n.debugId]=1,(0,se.u)(r);var i=(0,ae.YM)(n),s=f.gm.XMLHttpRequest,o=f.gm.MutationObserver,a=f.gm.Promise,c=f.gm.setInterval,d="readystatechange",u=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],l=[],p=f.gm.XMLHttpRequest=function(e){const r=new s(e),o=n.context(r);o.targets=(0,H.$5)(t);try{n.emit("new-xhr",[r],o),r.addEventListener(d,(a=o,function(){var e=this;e.readyState>3&&!a.resolved&&(a.resolved=!0,n.emit("xhr-resolved",[],e)),i.inPlace(e,u,"fn-",w)}),(0,N.jT)(!1))}catch(e){(0,h.R)(15,e);try{n.emit("internal-error",[e])}catch(e){}}var a;return r};function g(e,t){i.inPlace(t,["onreadystatechange"],"fn-",w)}if(function(e,t){for(var r in e)t[r]=e[r]}(s,p),p.prototype=s.prototype,i.inPlace(p.prototype,de,"-xhr-",w),n.on("send-xhr-start",function(e,t){g(e,t),function(e){l.push(e),o&&(m?m.then(b):c?c(b):(v=-v,y.data=v))}(t)}),n.on("open-xhr-start",g),o){var m=a&&a.resolve();if(!c&&!a){var v=1,y=document.createTextNode(v);new o(b).observe(y,{characterData:!0})}}else r.on("fn-end",function(e){e[0]&&e[0].type===d||b()});function b(){for(var e=0;e<l.length;e++)g(0,l[e]);l.length&&(l=[])}function w(e,t){return t}return n}var le="fetch-",fe=le+"body-",he=["arrayBuffer","blob","json","text","formData"],pe=f.gm.Request,ge=f.gm.Response,me="prototype";const ve={};function ye(e,t){const r=function(e){return(e||oe.ee).get("fetch")}(e);if(!(pe&&ge&&f.gm.fetch))return r;if(ve[r.debugId]++)return r;function n(e,n,i){var s=e[n];"function"==typeof s&&(e[n]=function(){var e=[...arguments];const n={},o=(0,H.$5)(t);var a;r.emit(i+"before-start",[e],n),n[oe.P]&&n[oe.P].dt&&(a=n[oe.P].dt);var c=s.apply(this,e);return r.emit(i+"start",[e,a],c),c.then(function(e){return r.emit(i+"end",[null,e,o],c),e},function(e){throw r.emit(i+"end",[e,void 0,o],c),e})})}return ve[r.debugId]=1,he.forEach(e=>{n(pe[me],e,fe),n(ge[me],e,fe)}),n(f.gm,"fetch",le),r.on(le+"end",function(e,t,n){var i=this;if(i.targets=n||[void 0],t){var s=t.headers.get("content-length");null!==s&&(i.rxSize=s),r.emit(le+"done",[null,t],i)}else r.emit(le+"done",[e],i)}),r}var be=i(7485);class we{constructor(e){this.agentRef=e}generateTracePayload(e){const t=this.agentRef.loader\_config;if(!this.shouldGenerateTrace(e)||!t)return null;var r=(t.accountID||"").toString()||null,n=(t.agentID||"").toString()||null,i=(t.trustKey||"").toString()||null;if(!r||!n)return null;var s=(0,Y.ZF)(),o=(0,Y.el)(),a=Date.now(),c={spanId:s,traceId:o,timestamp:a};return(e.sameOrigin||this.isAllowedOrigin(e)&&this.useTraceContextHeadersForCors())&&(c.traceContextParentHeader=this.generateTraceContextParentHeader(s,o),c.traceContextStateHeader=this.generateTraceContextStateHeader(s,a,r,n,i)),(e.sameOrigin&&!this.excludeNewrelicHeader()||!e.sameOrigin&&this.isAllowedOrigin(e)&&this.useNewrelicHeaderForCors())&&(c.newrelicHeader=this.generateTraceHeader(s,o,a,r,n,i)),c}generateTraceContextParentHeader(e,t){return"00-"+t+"-"+e+"-01"}generateTraceContextStateHeader(e,t,r,n,i){return i+"@nr=0-1-"+r+"-"+n+"-"+e+"----"+t}generateTraceHeader(e,t,r,n,i,s){if(!("function"==typeof f.gm?.btoa))return null;var o={v:[0,1],d:{ty:"Browser",ac:n,ap:i,id:e,tr:t,ti:r}};return s&&n!==s&&(o.d.tk=s),btoa((0,j.A)(o))}shouldGenerateTrace(e){return this.agentRef.init?.distributed\_tracing?.enabled&&this.isAllowedOrigin(e)}isAllowedOrigin(e){var t=!1;const r=this.agentRef.init?.distributed\_tracing;if(e.sameOrigin)t=!0;else if(r?.allowed\_origins instanceof Array)for(var n=0;n<r.allowed\_origins.length;n++){var i=(0,be.D)(r.allowed\_origins[n]);if(e.hostname===i.hostname&&e.protocol===i.protocol&&e.port===i.port){t=!0;break}}return t}excludeNewrelicHeader(){var e=this.agentRef.init?.distributed\_tracing;return!!e&&!!e.exclude\_newrelic\_header}useNewrelicHeaderForCors(){var e=this.agentRef.init?.distributed\_tracing;return!!e&&!1!==e.cors\_use\_newrelic\_header}useTraceContextHeadersForCors(){var e=this.agentRef.init?.distributed\_tracing;return!!e&&!!e.cors\_use\_tracecontext\_headers}}var Re=i(9300),Ee=i(7295);function Te(e){return"string"==typeof e?e:e instanceof(0,T.dV)().o.REQ?e.url:f.gm?.URL&&e instanceof URL?e.href:void 0}var Ae=["load","error","abort","timeout"],xe=Ae.length,Se=(0,T.dV)().o.REQ,\_e=(0,T.dV)().o.XHR;const Oe="X-NewRelic-App-Data";class Pe extends y{static featureName=Re.T;constructor(e){super(e,Re.T),this.dt=new we(e),this.handler=(e,t,r,n)=>(0,s.p)(e,t,r,n,this.ee);try{const e={xmlhttprequest:"xhr",fetch:"fetch",beacon:"beacon"};f.gm?.performance?.getEntriesByType("resource").forEach(r=>{if(r.initiatorType in e&&0!==r.responseStatus){const n={status:r.responseStatus},i={rxSize:r.transferSize,duration:Math.floor(r.duration),cbTime:0};ke(n,r.name),this.handler("xhr",[n,i,r.startTime,r.responseEnd,e[r.initiatorType]],void 0,t.K7.ajax)}})}catch(e){}ye(this.ee,e),ue(this.ee,e),function(e,r,n,i){function a(e){var t=this;t.totalCbs=0,t.called=0,t.cbTime=0,t.end=T,t.ended=!1,t.xhrGuids={},t.lastSize=null,t.loadCaptureCalled=!1,t.params=this.params||{},t.metrics=this.metrics||{},t.latestLongtaskEnd=0,e.addEventListener("load",function(r){x(t,e)},(0,N.jT)(!1)),f.lR||e.addEventListener("progress",function(e){t.lastSize=e.loaded},(0,N.jT)(!1))}function c(e){this.params={method:e[0]},ke(this,e[1]),this.metrics={}}function d(t,r){e.loader\_config.xpid&&this.sameOrigin&&r.setRequestHeader("X-NewRelic-ID",e.loader\_config.xpid);var n=i.generateTracePayload(this.parsedOrigin);if(n){var s=!1;n.newrelicHeader&&(r.setRequestHeader("newrelic",n.newrelicHeader),s=!0),n.traceContextParentHeader&&(r.setRequestHeader("traceparent",n.traceContextParentHeader),n.traceContextStateHeader&&r.setRequestHeader("tracestate",n.traceContextStateHeader),s=!0),s&&(this.dt=n)}}function u(e,t){var n=this.metrics,i=e[0],s=this;if(n&&i){var a=ie(i);a&&(n.txSize=a)}this.startTime=(0,o.t)(),this.body=i,this.listener=function(e){try{"abort"!==e.type||s.loadCaptureCalled||(s.params.aborted=!0),("load"!==e.type||s.called===s.totalCbs&&(s.onloadCalled||"function"!=typeof t.onload)&&"function"==typeof s.end)&&s.end(t)}catch(e){try{r.emit("internal-error",[e])}catch(e){}}};for(var c=0;c<xe;c++)t.addEventListener(Ae[c],this.listener,(0,N.jT)(!1))}function l(e,t,r){this.cbTime+=e,t?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof r.onload||"function"!=typeof this.end||this.end(r)}function h(e,t){var r=""+ne(e)+!!t;this.xhrGuids&&!this.xhrGuids[r]&&(this.xhrGuids[r]=!0,this.totalCbs+=1)}function p(e,t){var r=""+ne(e)+!!t;this.xhrGuids&&this.xhrGuids[r]&&(delete this.xhrGuids[r],this.totalCbs-=1)}function g(){this.endTime=(0,o.t)()}function m(e,t){t instanceof \_e&&"load"===e[0]&&r.emit("xhr-load-added",[e[1],e[2]],t)}function v(e,t){t instanceof \_e&&"load"===e[0]&&r.emit("xhr-load-removed",[e[1],e[2]],t)}function y(e,t,r){t instanceof \_e&&("onload"===r&&(this.onload=!0),("load"===(e[0]&&e[0].type)||this.onload)&&(this.xhrCbStart=(0,o.t)()))}function b(e,t){this.xhrCbStart&&r.emit("xhr-cb-time",[(0,o.t)()-this.xhrCbStart,this.onload,t],t)}function w(e){var t,r=e[1]||{};if("string"==typeof e[0]?0===(t=e[0]).length&&f.RI&&(t=""+f.gm.location.href):e[0]&&e[0].url?t=e[0].url:f.gm?.URL&&e[0]&&e[0]instanceof URL?t=e[0].href:"function"==typeof e[0].toString&&(t=e[0].toString()),"string"==typeof t&&0!==t.length){t&&(this.parsedOrigin=(0,be.D)(t),this.sameOrigin=this.parsedOrigin.sameOrigin);var n=i.generateTracePayload(this.parsedOrigin);if(n&&(n.newrelicHeader||n.traceContextParentHeader))if(e[0]&&e[0].headers)a(e[0].headers,n)&&(this.dt=n);else{var s={};for(var o in r)s[o]=r[o];s.headers=new Headers(r.headers||{}),a(s.headers,n)&&(this.dt=n),e.length>1?e[1]=s:e.push(s)}}function a(e,t){var r=!1;return t.newrelicHeader&&(e.set("newrelic",t.newrelicHeader),r=!0),t.traceContextParentHeader&&(e.set("traceparent",t.traceContextParentHeader),t.traceContextStateHeader&&e.set("tracestate",t.traceContextStateHeader),r=!0),r}}function R(e,t){this.params={},this.metrics={},this.startTime=(0,o.t)(),this.dt=t;let[r,n={}]=e;ke(this,Te(r));const i=(""+(r&&r instanceof Se&&r.method||n.method||"GET")).toUpperCase();this.params.method=i,this.body=n.body,this.txSize=ie(n.body)||0}function E(e,t){if(this.endTime=(0,o.t)(),this.params||(this.params={}),(0,Ee.iW)(this.params))return;let r;this.params.status=t?t.status:0,"string"==typeof this.rxSize&&this.rxSize.length>0&&(r=+this.rxSize);const n={txSize:this.txSize,rxSize:r,duration:(0,o.t)()-this.startTime},i=[this.params,n,this.startTime,this.endTime,"fetch"];this.targets.forEach(e=>A(i,this,e))}function T(e){const t=this.params,r=this.metrics;if(this.ended)return;this.ended=!0;for(let t=0;t<xe;t++)e.removeEventListener(Ae[t],this.listener,!1);if(t.aborted)return;if((0,Ee.iW)(t))return;r.duration=(0,o.t)()-this.startTime,this.loadCaptureCalled||4!==e.readyState?null==t.status&&(t.status=0):x(this,e),r.cbTime=this.cbTime;const n=[t,r,this.startTime,this.endTime,"xhr"];this.targets.forEach(e=>A(n,this,e))}function A(e,r,i){n("xhr",[...e,i],r,t.K7.ajax)}function x(e,n){e.params.status=n.status;var i=function(e,t){var r=e.responseType;return"json"===r&&null!==t?t:"arraybuffer"===r||"blob"===r||"json"===r?ie(e.response):"text"===r||""===r||void 0===r?ie(e.responseText):void 0}(n,e.lastSize);if(i&&(e.metrics.rxSize=i),e.sameOrigin&&n.getAllResponseHeaders().indexOf(Oe)>=0){var o=n.getResponseHeader(Oe);o&&((0,s.p)(O.rs,["Ajax/CrossApplicationTracing/Header/Seen"],void 0,t.K7.metrics,r),e.params.cat=o.split(", ").pop())}e.loadCaptureCalled=!0}r.on("new-xhr",a),r.on("open-xhr-start",c),r.on("open-xhr-end",d),r.on("send-xhr-start",u),r.on("xhr-cb-time",l),r.on("xhr-load-added",h),r.on("xhr-load-removed",p),r.on("xhr-resolved",g),r.on("addEventListener-end",m),r.on("removeEventListener-end",v),r.on("fn-end",b),r.on("fetch-before-start",w),r.on("fetch-start",R),r.on("fn-start",y),r.on("fetch-done",E)}(e,this.ee,this.handler,this.dt),this.importAggregator(e,()=>i.e(478).then(i.bind(i,3845)))}}function ke(e,t){var r=(0,be.D)(t),n=e.params||e;n.hostname=r.hostname,n.port=r.port,n.protocol=r.protocol,n.host=r.hostname+":"+r.port,n.pathname=r.pathname,e.parsedOrigin=r,e.sameOrigin=r.sameOrigin}const Ne={},je=["pushState","replaceState"];function De(e){const t=function(e){return(e||oe.ee).get("history")}(e);return!f.RI||Ne[t.debugId]++||(Ne[t.debugId]=1,(0,ae.YM)(t).inPlace(window.history,je,"-")),t}var Ce=i(3738);function Le(e){(0,c.Y)(a.BL,function(r=Date.now()){const n=r-f.WN;n<0&&(0,h.R)(62,r),(0,s.p)(O.XG,[a.BL,{time:n}],void 0,t.K7.metrics,e.ee),e.addToTrace({name:a.BL,start:r,origin:"nr"}),(0,s.p)(a.Pl+a.hG,[n,a.BL],void 0,t.K7.genericEvents,e.ee)},e)}const{He:Ie,bD:Me,d3:Be,Kp:He,TZ:Ke,Lc:We,uP:Fe,Rz:Ue}=Ce;class Ve extends y{static featureName=Ke;constructor(e){var r;super(e,Ke),r=e,(0,c.Y)(a.U2,function(e){if(!(e&&"object"==typeof e&&e.name&&e.start))return;const n={n:e.name,s:e.start-f.WN,e:(e.end||e.start)-f.WN,o:e.origin||"",t:"api"};n.s<0||n.e<0||n.e<n.s?(0,h.R)(61,{start:n.s,end:n.e}):(0,s.p)("bstApi",[n],void 0,t.K7.sessionTrace,r.ee)},r),Le(e);if(!(0,g.V)(e.init))return void this.deregisterDrain();const n=this.ee;let d;De(n),this.eventsEE=(0,se.u)(n),this.eventsEE.on(Fe,function(e,t){this.bstStart=(0,o.t)()}),this.eventsEE.on(We,function(e,r){(0,s.p)("bst",[e[0],r,this.bstStart,(0,o.t)()],void 0,t.K7.sessionTrace,n)}),n.on(Ue+Be,function(e){this.time=(0,o.t)(),this.startPath=location.pathname+location.hash}),n.on(Ue+He,function(e){(0,s.p)("bstHist",[location.pathname+location.hash,this.startPath,this.time],void 0,t.K7.sessionTrace,n)});try{d=new PerformanceObserver(e=>{const r=e.getEntries();(0,s.p)(Ie,[r],void 0,t.K7.sessionTrace,n)}),d.observe({type:Me,buffered:!0})}catch(e){}this.importAggregator(e,()=>i.e(478).then(i.bind(i,6974)),{resourceObserver:d})}}var ze=i(6344);class Ge extends y{static featureName=ze.TZ;#n;recorder;constructor(e){var r;let n;super(e,ze.TZ),r=e,(0,c.Y)(a.CH,function(){(0,s.p)(a.CH,[],void 0,t.K7.sessionReplay,r.ee)},r),function(e){(0,c.Y)(a.Tb,function(){(0,s.p)(a.Tb,[],void 0,t.K7.sessionReplay,e.ee)},e)}(e);try{n=JSON.parse(localStorage.getItem("".concat(w.H3,"\_").concat(w.uh)))}catch(e){}(0,p.SR)(e.init)&&this.ee.on(a.CH,()=>this.#i()),this.#s(n)&&this.importRecorder().then(e=>{e.startRecording(ze.Qb.PRELOAD,n?.sessionReplayMode)}),this.importAggregator(this.agentRef,()=>i.e(478).then(i.bind(i,6167)),this),this.ee.on("err",e=>{this.blocked||this.agentRef.runtime.isRecording&&(this.errorNoticed=!0,(0,s.p)(ze.Vh,[e],void 0,this.featureName,this.ee))})}#s(e){return e&&(e.sessionReplayMode===w.g.FULL||e.sessionReplayMode===w.g.ERROR)||(0,p.Aw)(this.agentRef.init)}importRecorder(){return this.recorder?Promise.resolve(this.recorder):(this.#n??=Promise.all([i.e(478),i.e(249)]).then(i.bind(i,4866)).then(({Recorder:e})=>(this.recorder=new e(this),this.recorder)).catch(e=>{throw this.ee.emit("internal-error",[e]),this.blocked=!0,e}),this.#n)}#i(){this.blocked||(this.featAggregate?this.featAggregate.mode!==w.g.FULL&&this.featAggregate.initializeRecording(w.g.FULL,!0,ze.Qb.API):this.importRecorder().then(()=>{this.recorder.startRecording(ze.Qb.API,w.g.FULL)}))}}var Ye=i(3962);class Ze extends y{static featureName=Ye.TZ;constructor(e){if(super(e,Ye.TZ),function(e){const r=e.ee.get("tracer");function n(){}(0,c.Y)(a.dT,function(e){return(new n).get("object"==typeof e?e:{})},e);const i=n.prototype={createTracer:function(n,i){var a={},c=this,d="function"==typeof i;return(0,s.p)(O.xV,["API/createTracer/called"],void 0,t.K7.metrics,e.ee),function(){if(r.emit((d?"":"no-")+"fn-start",[(0,o.t)(),c,d],a),d)try{return i.apply(this,arguments)}catch(e){const t="string"==typeof e?new Error(e):e;throw r.emit("fn-err",[arguments,this,t],a),t}finally{r.emit("fn-end",[(0,o.t)()],a)}}}};["actionText","setName","setAttribute","save","ignore","onEnd","getContext","end","get"].forEach(r=>{c.Y.apply(this,[r,function(){return(0,s.p)(a.hw+r,[performance.now(),...arguments],this,t.K7.softNav,e.ee),this},e,i])}),(0,c.Y)(a.PA,function(){(0,s.p)(a.hw+"routeName",[performance.now(),...arguments],void 0,t.K7.softNav,e.ee)},e)}(e),!f.RI||!(0,T.dV)().o.MO)return;const r=De(this.ee);try{this.removeOnAbort=new AbortController}catch(e){}Ye.tC.forEach(e=>{(0,N.sp)(e,e=>{l(e)},!0,this.removeOnAbort?.signal)});const n=()=>(0,s.p)("newURL",[(0,o.t)(),""+window.location],void 0,this.featureName,this.ee);r.on("pushState-end",n),r.on("replaceState-end",n),(0,N.sp)(Ye.OV,e=>{l(e),(0,s.p)("newURL",[e.timeStamp,""+window.location],void 0,this.featureName,this.ee)},!0,this.removeOnAbort?.signal);let d=!1;const u=new((0,T.dV)().o.MO)((e,t)=>{d||(d=!0,requestAnimationFrame(()=>{(0,s.p)("newDom",[(0,o.t)()],void 0,this.featureName,this.ee),d=!1}))}),l=(0,m.s)(e=>{"loading"!==document.readyState&&((0,s.p)("newUIEvent",[e],void 0,this.featureName,this.ee),u.observe(document.body,{attributes:!0,childList:!0,subtree:!0,characterData:!0}))},100,{leading:!0});this.abortHandler=function(){this.removeOnAbort?.abort(),u.disconnect(),this.abortHandler=void 0},this.importAggregator(e,()=>i.e(478).then(i.bind(i,4393)),{domObserver:u})}}var qe=i(3333),Xe=i(9119);const $e={},Qe=new Set;function Je(e){return"string"==typeof e?{type:"string",size:(new TextEncoder).encode(e).length}:e instanceof ArrayBuffer?{type:"ArrayBuffer",size:e.byteLength}:e instanceof Blob?{type:"Blob",size:e.size}:e instanceof DataView?{type:"DataView",size:e.byteLength}:ArrayBuffer.isView(e)?{type:"TypedArray",size:e.byteLength}:{type:"unknown",size:0}}class et{constructor(e,t){this.timestamp=(0,o.t)(),this.currentUrl=(0,Xe.L)(window.location.href),this.socketId=(0,Y.LA)(8),this.requestedUrl=(0,Xe.L)(e),this.requestedProtocols=Array.isArray(t)?t.join(","):t||"",this.openedAt=void 0,this.protocol=void 0,this.extensions=void 0,this.binaryType=void 0,this.messageOrigin=void 0,this.messageCount=0,this.messageBytes=0,this.messageBytesMin=0,this.messageBytesMax=0,this.messageTypes=void 0,this.sendCount=0,this.sendBytes=0,this.sendBytesMin=0,this.sendBytesMax=0,this.sendTypes=void 0,this.closedAt=void 0,this.closeCode=void 0,this.closeReason="unknown",this.closeWasClean=void 0,this.connectedDuration=0,this.hasErrors=void 0}}class tt extends y{static featureName=qe.TZ;constructor(e){super(e,qe.TZ);const r=e.init.feature\_flags.includes("websockets"),n=!e.init.feature\_flags.includes("no\_spv"),d=[e.init.page\_action.enabled,e.init.performance.capture\_marks,e.init.performance.capture\_measures,e.init.performance.resources.enabled,e.init.user\_actions.enabled,r,n];var u;let l;if(u=e,(0,c.Y)(a.hG,(e,t)=>U(e,t,u),u),function(e){(0,c.Y)(a.fF,(t,r)=>z(t,r,e),e)}(e),Le(e),Q(e),function(e){(0,c.Y)(a.V1,(t,r)=>V(t,r,e),e)}(e),this.removeOnAbort=new AbortController,this.abortHandler=()=>{this.removeOnAbort.abort(),this.abortHandler=void 0},r){const h=function(e){if(!(0,T.dV)().o.WS)return e;const t=e.get("websockets");if($e[t.debugId]++)return t;$e[t.debugId]=1,(0,x.G)(()=>{const e=(0,o.t)();Qe.forEach(r=>{r.nrData.closedAt=e,r.nrData.closeCode=1001,r.nrData.closeReason="Page navigating away",r.nrData.closeWasClean=!1,r.nrData.openedAt&&(r.nrData.connectedDuration=e-r.nrData.openedAt),t.emit("ws",[r.nrData],r)})});class r extends WebSocket{static name="WebSocket";static toString(){return"function WebSocket() { [native code] }"}toString(){return"[object WebSocket]"}get[Symbol.toStringTag](){return r.name}#o(e){(e.\_\_newrelic??={}).socketId=this.nrData.socketId,this.nrData.hasErrors??=!0}constructor(...e){super(...e),this.nrData=new et(e[0],e[1]),this.addEventListener("open",()=>{this.nrData.openedAt=(0,o.t)(),["protocol","extensions","binaryType"].forEach(e=>{this.nrData[e]=this[e]}),Qe.add(this)}),this.addEventListener("message",e=>{const{type:t,size:r}=Je(e.data);this.nrData.messageOrigin??=(0,Xe.L)(e.origin),this.nrData.messageCount++,this.nrData.messageBytes+=r,this.nrData.messageBytesMin=Math.min(this.nrData.messageBytesMin||1/0,r),this.nrData.messageBytesMax=Math.max(this.nrData.messageBytesMax,r),(this.nrData.messageTypes??"").includes(t)||(this.nrData.messageTypes=this.nrData.messageTypes?"".concat(this.nrData.messageTypes,",").concat(t):t)}),this.addEventListener("close",e=>{this.nrData.closedAt=(0,o.t)(),this.nrData.closeCode=e.code,e.reason&&(this.nrData.closeReason=e.reason),this.nrData.closeWasClean=e.wasClean,this.nrData.connectedDuration=this.nrData.closedAt-this.nrData.openedAt,Qe.delete(this),t.emit("ws",[this.nrData],this)})}addEventListener(e,t,...r){const n=this,i="function"==typeof t?function(...e){try{return t.apply(this,e)}catch(e){throw n.#o(e),e}}:t?.handleEvent?{handleEvent:function(...e){try{return t.handleEvent.apply(t,e)}catch(e){throw n.#o(e),e}}}:t;return super.addEventListener(e,i,...r)}send(e){if(this.readyState===WebSocket.OPEN){const{type:t,size:r}=Je(e);this.nrData.sendCount++,this.nrData.sendBytes+=r,this.nrData.sendBytesMin=Math.min(this.nrData.sendBytesMin||1/0,r),this.nrData.sendBytesMax=Math.max(this.nrData.sendBytesMax,r),(this.nrData.sendTypes??"").includes(t)||(this.nrData.sendTypes=this.nrData.sendTypes?"".concat(this.nrData.sendTypes,",").concat(t):t)}try{return super.send(e)}catch(e){throw this.#o(e),e}}close(...e){try{super.close(...e)}catch(e){throw this.#o(e),e}}}return f.gm.WebSocket=r,t}(this.ee);h.on("ws",e=>{(0,s.p)("ws-complete",[e],void 0,this.featureName,this.ee)})}if(n&&f.gm.addEventListener("securitypolicyviolation",e=>{(0,s.p)("spv",[e],void 0,t.K7.genericEvents,this.ee)},(0,N.jT)(!1,this.removeOnAbort.signal)),f.RI){if(ye(this.ee,e),ue(this.ee,e),l=De(this.ee),e.init.user\_actions.enabled){function p(t){const r=(0,be.D)(t);return e.beacons.includes(r.hostname+":"+r.port)}function g(){l.emit("navChange")}qe.Zp.forEach(e=>(0,N.sp)(e,e=>(0,s.p)("ua",[e],void 0,this.featureName,this.ee),!0)),qe.qN.forEach(e=>{const t=(0,m.s)(e=>{(0,s.p)("ua",[e],void 0,this.featureName,this.ee)},500,{leading:!0});(0,N.sp)(e,t)}),f.gm.addEventListener("error",()=>{(0,s.p)("uaErr",[],void 0,t.K7.genericEvents,this.ee)},(0,N.jT)(!1,this.removeOnAbort.signal)),this.ee.on("open-xhr-start",(e,r)=>{p(e[1])||r.addEventListener("readystatechange",()=>{2===r.readyState&&(0,s.p)("uaXhr",[],void 0,t.K7.genericEvents,this.ee)},(0,N.jT)(void 0,this.removeOnAbort.signal))}),this.ee.on("fetch-start",e=>{e.length>=1&&!p(Te(e[0]))&&(0,s.p)("uaXhr",[],void 0,t.K7.genericEvents,this.ee)}),l.on("pushState-end",g),l.on("replaceState-end",g),window.addEventListener("hashchange",g,(0,N.jT)(!0,this.removeOnAbort.signal)),window.addEventListener("popstate",g,(0,N.jT)(!0,this.removeOnAbort.signal))}if(e.init.performance.resources.enabled&&f.gm.PerformanceObserver?.supportedEntryTypes.includes("resource")){new PerformanceObserver(e=>{e.getEntries().forEach(e=>{(0,s.p)("browserPerformance.resource",[e],void 0,this.featureName,this.ee)})}).observe({type:"resource",buffered:!0})}}d.some(e=>e)?this.importAggregator(e,()=>i.e(478).then(i.bind(i,8019))):this.deregisterDrain()}}var rt=i(2646);const nt=new Map;function it(e,t,r,n,i=!0,s){if("object"!=typeof t||!t||"string"!=typeof r||!r||"function"!=typeof t[r])return(0,h.R)(29);const o=function(e){return(e||oe.ee).get("logger")}(e),a=(0,ae.YM)(o,void 0,s),c=new rt.y(oe.P);c.level=n.level,c.customAttributes=n.customAttributes,c.autoCaptured=i;const d=t[r]?.[ae.Jt]||t[r];return nt.set(d,c),a.inPlace(t,[r],"wrap-logger-",()=>nt.get(d),void 0,!0),o}var st=i(1910);class ot extends y{static featureName=K.TZ;constructor(e){var t;super(e,K.TZ),t=e,(0,c.Y)(a.$9,(e,r)=>F(e,r,t),t),function(e){(0,c.Y)(a.Wb,(t,r,{customAttributes:n={},level:i=K.p\_.INFO}={})=>{it(e.ee,t,r,{customAttributes:n,level:i},!1,e)},e)}(e),Q(e);const r=this.ee;["log","error","warn","info","debug","trace"].forEach(t=>{(0,st.i)(f.gm.console[t]),it(r,f.gm.console,t,{level:"log"===t?"info":t},void 0,e)}),this.ee.on("wrap-logger-end",function([e],t,n,i=[]){const{level:s,customAttributes:o,autoCaptured:a}=this;i.forEach(t=>{(0,W.R)(r,e,o,s,a,t)})}),this.importAggregator(e,()=>i.e(478).then(i.bind(i,5288)))}}new A({features:[Pe,E,\_,Ve,Ge,P,ee,tt,ot,Ze],loaderType:"spa"})})()})();
































{"@context":"https://schema.org","@graph":[{"@type":"Corporation","@id":"https://www.docker.com/#organization","name":"Docker","url":"https://www.docker.com","sameAs":["https://www.facebook.com/docker.run","https://twitter.com/Docker"],"logo":{"@type":"ImageObject","@id":"https://www.docker.com/#logo","url":"https://www.docker.com/app/uploads/2022/05/Docker\_Temporary\_Image\_Google\_Blue\_1080x1080\_v1.png","contentUrl":"https://www.docker.com/app/uploads/2022/05/Docker\_Temporary\_Image\_Google\_Blue\_1080x1080\_v1.png","caption":"Docker","inLanguage":"en-US"}},{"@type":"WebSite","@id":"https://www.docker.com/#website","url":"https://www.docker.com","name":"Docker","publisher":{"@id":"https://www.docker.com/#organization"},"inLanguage":"en-US"},{"@type":"ImageObject","@id":"https://www.docker.com/app/uploads/2025/03/image.png","url":"https://www.docker.com/app/uploads/2025/03/image.png","width":"1300","height":"1300","caption":"Featured image","inLanguage":"en-US"},{"@type":"WebPage","@id":"https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/#webpage","url":"https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/","name":"Deterministic AI Testing with Session Recording in cagent | Docker","datePublished":"2026-01-06T11:16:04-08:00","dateModified":"2026-01-09T10:19:52-08:00","isPartOf":{"@id":"https://www.docker.com/#website"},"primaryImageOfPage":{"@id":"https://www.docker.com/app/uploads/2025/03/image.png"},"inLanguage":"en-US"},{"@type":"BlogPosting","headline":"Deterministic AI Testing with Session Recording in cagent | Docker","datePublished":"2026-01-06T11:16:04-08:00","dateModified":"2026-01-09T10:19:52-08:00","author":{"@id":"https://www.docker.com/contributors/stan-hamara/#Person"},"publisher":{"@id":"https://www.docker.com/#organization"},"description":"Learn from Docker experts to simplify and advance your app development and management with Docker. Stay up to date on Docker events and new version","name":"Deterministic AI Testing with Session Recording in cagent | Docker","@id":"https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/#richSnippet","isPartOf":{"@id":"https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/#webpage"},"image":{"@id":"https://www.docker.com/app/uploads/2025/03/image.png"},"inLanguage":"en-US","mainEntityOfPage":{"@id":"https://www.docker.com/blog/deterministic-ai-testing-with-session-recording-in-cagent/#webpage"}},{"@type":"Person","@id":"https://www.docker.com/contributors/stan-hamara/#Person","name":"Stan Hamara","url":"https://www.docker.com/contributors/stan-hamara/","jobTitle":"Senior Software Engineer","image":{"@type":"ImageObject","@id":"https://www.docker.com/app/uploads/2025/11/E7UHBTE03-U060BELD491-fd981966469e-512.jpeg","url":"https://www.docker.com/app/uploads/2025/11/E7UHBTE03-U060BELD491-fd981966469e-512.jpeg","caption":"Stan Hamara","inLanguage":"en-US","width":"512","height":"512"},"identifier":{"@type":"PropertyValue","name":"Docker Author ID","value":"stan-hamara"},"sameAs":[],"worksFor":{"@id":"https://www.docker.com/#organization"}}]}

Deterministic AI Testing with Session Recording in cagent | Docker





img:is([sizes=auto i],[sizes^="auto," i]){contain-intrinsic-size:3000px 1500px}
/\*# sourceURL=wp-img-auto-sizes-contain-inline-css \*/

.wp-block-ponyo-megan .toggle{align-items:center;background:none;border:0;cursor:pointer;display:flex!important;justify-content:space-between}@media screen and (min-width:61.25rem){.wp-block-ponyo-megan .toggle{gap:.25em;justify-content:normal}}.wp-block-ponyo-megan .toggle-icon{height:1rem;margin-top:.075em;width:1rem}@media screen and (min-width:61.25rem){.wp-block-ponyo-megan .toggle-icon{height:.75rem;width:.75rem}}.wp-block-ponyo-megan .toggle-icon svg{stroke:currentColor;transition:transform .3s ease}.wp-block-ponyo-megan .mega-menu-container{background-color:var(--headerBackgroundColor);height:0;opacity:0;overflow:hidden;visibility:hidden}@media screen and (min-width:61.25rem){.wp-block-ponyo-megan .mega-menu-container{border:0;box-shadow:0 50px 40px 0 rgba(0,0,0,.14);height:auto;left:0;position:absolute;right:0;top:100%;transition:opacity .2s ease,visibility .1s .2s,overflow .1s .2s;width:100%}.wp-block-ponyo-megan:hover .toggle-icon svg{transform:rotate(180deg)}.wp-block-ponyo-megan:hover .mega-menu-container{height:auto;opacity:1;overflow:visible;transition:opacity .4s ease;visibility:visible}}@media screen and (max-width:61.1875rem){.wp-block-ponyo-megan.mega-menu-active .toggle-icon svg{transform:rotate(180deg)}.wp-block-ponyo-megan.mega-menu-active .mega-menu-container{height:auto;opacity:1;overflow:visible;visibility:visible}}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/organisms/megan/megan-style.css \*/

@media screen and (min-width:61.25rem){.wp-block-ponyo-melinda{width:50%}}.wp-block-ponyo-melinda a{display:block;outline-offset:.25rem;padding:.75rem 1rem .5rem}.wp-block-ponyo-melinda a:hover{background-color:var(--menuLinkHover);text-decoration:none}.wp-block-ponyo-melinda a:active{background-color:var(--menuLinkActive)}.wp-block-ponyo-melinda:not(.button:last-child) a{display:flex;gap:.75rem}.wp-block-ponyo-melinda:not(.button:last-child) a:hover .label{color:var(--menuLinkHoverLabelColor)}.wp-block-ponyo-melinda:not(.button:last-child) a:hover .arrow{opacity:1;transform:translateX(0)}.wp-block-ponyo-melinda:not(.button:last-child) .label{color:var(--menuLinkLabelColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:.875rem;font-weight:400;font-weight:500;letter-spacing:-.15px;line-height:130%;margin-bottom:0;max-width:72ch;transition:all .3s}.wp-block-ponyo-melinda:not(.button:last-child) svg.arrow{opacity:0;transform:translateX(-50%);transition:all .1s}.wp-block-ponyo-melinda.button:last-child{justify-content:center;margin-top:auto}.wp-block-ponyo-melinda.button:last-child a:hover .label{text-decoration:underline}.wp-block-ponyo-melinda.button:last-child .label{font-size:1rem;justify-content:center;width:100%}.wp-block-ponyo-melinda .label{align-items:center;display:inline-flex;gap:.5rem;line-height:1.3}.wp-block-ponyo-melinda svg.external-link{flex-shrink:0;height:1.25rem;width:1.25rem}.wp-block-ponyo-melinda svg.arrow{width:.5rem}.wp-block-ponyo-melinda .description{color:var(--menuLinkDescriptionColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:.875rem;font-weight:400;letter-spacing:-.15px;line-height:130%;margin-bottom:0;max-width:72ch}.wp-block-ponyo-melinda .wp-block-ponyo-icon{flex-shrink:0;padding-top:.25rem}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/melinda/melinda-style.css \*/


.wp-block-ponyo-myles{flex-basis:58%;height:100%;padding:1.25rem 0 1.75rem}.wp-block-ponyo-myles ul{display:flex;flex-direction:column;flex-wrap:wrap;gap:.75rem}@media screen and (min-width:61.25rem){.wp-block-ponyo-myles ul{gap:unset;max-height:400px}}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/organisms/myles/myles-style.css \*/

.wp-block-ponyo-mainard{flex:1}.wp-block-ponyo-mainard:hover{text-decoration:none}.wp-block-ponyo-mainard img{aspect-ratio:2/1;border-radius:.5rem;margin-bottom:.75rem;max-height:180px;-o-object-fit:cover;object-fit:cover;overflow:hidden;width:100%}.wp-block-ponyo-mack.style\_\_multi .wp-block-ponyo-mainard img{max-height:100px}.wp-block-ponyo-mainard .title{color:var(--menuLinkLabelColor);font-size:.875rem}.wp-block-ponyo-mainard .excerpt,.wp-block-ponyo-mainard .title{font-family:Inter,Helvetica,Arial,sans-serif;font-weight:400;letter-spacing:-.15px;line-height:130%;max-width:72ch}.wp-block-ponyo-mainard .excerpt{color:var(--menuLinkDescriptionColor);font-size:.75rem;margin-bottom:.75rem}.wp-block-ponyo-mainard .link-text{align-items:center;display:inline-flex}.wp-block-ponyo-mainard .link-text svg{margin-left:.375rem;width:.5rem}.wp-block-ponyo-mainard .link-text{color:var(--buttonCtaText);font-family:Inter,Helvetica,Arial,sans-serif;font-size:.75rem;font-weight:400;font-weight:500;letter-spacing:-.15px;line-height:130%;max-width:72ch}.wp-block-ponyo-mainard:hover .link-text{color:var(--menuLinkHoverLabelColor)}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/mainard/mainard-style.css \*/

.wp-block-ponyo-mack{margin-bottom:1.5rem}@media screen and (min-width:48rem){.wp-block-ponyo-mack{flex-basis:40%;margin-bottom:0;padding:1.25rem 0 1.75rem 1.5rem}}.wp-block-ponyo-mack .label{flex-basis:50%;font-family:Inter,Helvetica,Arial,sans-serif;font-size:.875rem;font-weight:400;font-weight:500;letter-spacing:-.15px;line-height:130%;margin-bottom:.75rem;max-width:72ch;text-transform:uppercase}.wp-block-ponyo-mack .content{display:flex;flex-direction:column;gap:1.5rem}@media screen and (min-width:61.25rem){.wp-block-ponyo-mack .content{flex-direction:row}}.wp-block-ponyo-mack.no-label .content{padding-top:1.75rem}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/organisms/mack/mack-style.css \*/

.wp-block-ponyo-mikala{border-top:1px solid var(--menuBorderColor);margin:auto;max-width:1440px;padding:0 1.75rem;position:relative;width:100%}@media screen and (min-width:48rem){.wp-block-ponyo-mikala{display:flex;justify-content:space-between}}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/organisms/mikala/mikala-style.css \*/

.wp-block-ponyo-icon svg{height:100%;width:100%}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/atoms/icon/icon-style.css \*/

.wp-block-ponyo-button{background-color:var(--backgroundColor);border:1px solid var(--borderColor);color:var(--copyColor);position:relative;--iconColor:var(--copyColor);align-items:center;-moz-column-gap:.75rem;column-gap:.75rem;cursor:pointer;display:inline-flex;flex-direction:row;flex-wrap:wrap;font-family:Inter,Helvetica,Arial,sans-serif;font-size:.875rem;font-weight:400;font-weight:500;justify-content:center;letter-spacing:-.15px;line-height:130%;max-width:72ch;row-gap:.375rem;text-decoration:none;transition:all .25s ease}.wp-block-ponyo-button:hover{text-decoration:none}.wp-block-ponyo-button:focus{outline:4px solid var(--buttonPrimaryFocusOutline)}.disabled.wp-block-ponyo-button,.wp-block-ponyo-button:disabled{pointer-events:none}.wp-block-ponyo-button path,.wp-block-ponyo-button svg{transition:all .25s ease}.wp-block-ponyo-button .wp-block-ponyo-pill.style\_\_secondary{background-color:var(--copyColor);color:var(--backgroundColor);transition:all .25s ease}.wp-block-ponyo-button.button-style\_\_primary,.wp-block-ponyo-button.button-style\_\_secondary{overflow:hidden;position:relative;z-index:0}.wp-block-ponyo-button.button-size\_\_small{border-radius:.25rem;box-shadow:inset 0 0 1px 1px var(--shadowColor);padding:.5rem .75rem}.wp-block-ponyo-button.button-size\_\_small,.wp-block-ponyo-button.button-size\_\_small.button\_\_rounded{align-self:center;--iconSize:1rem;font-family:Inter,Helvetica,Arial,sans-serif;font-size:.75rem;font-weight:400;font-weight:500;letter-spacing:-.15px;line-height:130%;max-width:72ch}.wp-block-ponyo-button.button-size\_\_small.button\_\_rounded{border-radius:12.5rem;padding:.5rem}.wp-block-ponyo-button.button-size\_\_large{border-radius:.5rem;box-shadow:inset 0 0 1px 1px var(--shadowColor);padding:.75rem 1.25rem}.wp-block-ponyo-button.button-size\_\_large.button\_\_rounded{border-radius:12.5rem;padding:.75rem 1.25rem}.wp-block-ponyo-button.button-style\_\_primary{--backgroundColor:var(--buttonPrimaryBackground);--borderColor:var(--buttonPrimaryBorder);--borderWidth:var(--buttonPrimaryBorderWidth);--copyColor:var(--buttonPrimaryText);--shadowColor:var(--buttonPrimaryShadow)}.wp-block-ponyo-button.button-style\_\_primary:hover{--backgroundColor:var(--buttonPrimaryHoverBackground);--borderColor:var(--buttonPrimaryHoverBorder);--copyColor:var(--buttonPrimaryHoverText)}.wp-block-ponyo-button.button-style\_\_primary:active{--backgroundColor:var(--buttonPrimaryActiveBackground);--borderColor:var(--buttonPrimaryActiveBorder);--copyColor:var(--buttonPrimaryActiveText);--shadowColor:var(--buttonPrimaryActiveShadow)}.wp-block-ponyo-button.button-style\_\_primary:focus{--borderColor:var(--buttonPrimaryFocusBorder)}.wp-block-ponyo-button.button-style\_\_primary.disabled,.wp-block-ponyo-button.button-style\_\_primary:disabled{--backgroundColor:var(--buttonPrimaryDisabledBackground);--borderColor:var(--buttonPrimaryDisabledBorder);--copyColor:var(--buttonPrimaryDisabledText);--shadowColor:var(--buttonPrimaryDisabledShadow)}.wp-block-ponyo-button.button-style\_\_secondary{--backgroundColor:var(--buttonSecondaryBackground);--borderColor:var(--buttonSecondaryBorder);--borderWidth:var(--buttonSecondaryBorderWidth);--copyColor:var(--buttonSecondaryText);--shadowColor:var(--buttonSecondaryShadow)}.wp-block-ponyo-button.button-style\_\_secondary:hover{--backgroundColor:var(--buttonSecondaryHoverBackground);--borderColor:var(--buttonSecondaryHoverBorder);--copyColor:var(--buttonSecondaryHoverText)}.wp-block-ponyo-button.button-style\_\_secondary:active{--backgroundColor:var(--buttonSecondaryActiveBackground);--borderColor:var(--buttonSecondaryActiveBorder);--copyColor:var(--buttonSecondaryActiveText);--shadowColor:var(--buttonSecondaryActiveShadow)}.wp-block-ponyo-button.button-style\_\_secondary:focus{--borderColor:var(--buttonSecondaryFocusBorder)}.wp-block-ponyo-button.button-style\_\_secondary.disabled,.wp-block-ponyo-button.button-style\_\_secondary:disabled{--backgroundColor:var(--buttonSecondaryDisabledBackground);--borderColor:var(--buttonSecondaryDisabledBorder);--copyColor:var(--buttonSecondaryDisabledText);--shadowColor:var(--buttonSecondaryDisabledShadow)}.wp-block-ponyo-button.button-style\_\_tertiary{--backgroundColor:var(--buttonTertiaryBackground);--borderColor:var(--buttonTertiaryBorder);--borderWidth:var(--buttonTertiaryBorderWidth);--copyColor:var(--buttonTertiaryText);--shadowColor:var(--buttonTertiaryShadow)}.wp-block-ponyo-button.button-style\_\_tertiary:hover{--backgroundColor:var(--buttonTertiaryHoverBackground);--borderColor:var(--buttonTertiaryHoverBorder);--copyColor:var(--buttonTertiaryHoverText)}.wp-block-ponyo-button.button-style\_\_tertiary:active{--backgroundColor:var(--buttonTertiaryActiveBackground);--borderColor:var(--buttonTertiaryActiveBorder);--copyColor:var(--buttonTertiaryActiveText);--shadowColor:var(--buttonTertiaryActiveShadow)}.wp-block-ponyo-button.button-style\_\_tertiary:focus{--borderColor:var(--buttonTertiaryFocusBorder)}.wp-block-ponyo-button.button-style\_\_tertiary.disabled,.wp-block-ponyo-button.button-style\_\_tertiary:disabled{--backgroundColor:var(--buttonTertiaryDisabledBackground);--borderColor:var(--buttonTertiaryDisabledBorder);--copyColor:var(--buttonTertiaryDisabledText);--shadowColor:var(--buttonTertiaryDisabledShadow)}.wp-block-ponyo-button.button-style\_\_tertiary{border-radius:0;margin:.75rem 0;outline-offset:.25rem;padding:0}.wp-block-ponyo-button.button-style\_\_cta{--backgroundColor:transparent;--borderColor:var(--buttonCtaBorder);--borderWidth:var(--buttonCtaBorderWidth);--copyColor:var(--buttonCtaText);--shadowColor:var(--buttonCtaShadow)}.wp-block-ponyo-button.button-style\_\_cta:hover{--backgroundColor:transparent;--borderColor:var(--buttonCtaHoverBorder);--copyColor:var(--buttonCtaHoverText)}.wp-block-ponyo-button.button-style\_\_cta:active{--backgroundColor:var(--buttonCtaActiveBackground);--borderColor:var(--buttonCtaActiveBorder);--copyColor:var(--buttonCtaActiveText);--shadowColor:var(--buttonCtaActiveShadow)}.wp-block-ponyo-button.button-style\_\_cta:focus{--borderColor:var(--buttonCtaFocusBorder)}.wp-block-ponyo-button.button-style\_\_cta.disabled,.wp-block-ponyo-button.button-style\_\_cta:disabled{--backgroundColor:var(--buttonCtaDisabledBackground);--borderColor:var(--buttonCtaDisabledBorder);--copyColor:var(--buttonCtaDisabledText);--shadowColor:var(--buttonTCtaDisabledShadow)}.wp-block-ponyo-button.button-style\_\_cta{border-radius:0;margin:.75rem 0;outline-offset:.25rem;padding:0}.wp-block-ponyo-button.button-style\_\_cta svg.arrow{height:.75em}.wp-block-ponyo-button.button-style\_\_cta:hover svg.arrow{transform:translateX(.125em)}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/atoms/button/button-style.css \*/

.wp-block-ponyo-callie{display:flex;gap:.5rem}@media screen and (max-width:61.1875rem){.wp-block-ponyo-callie{flex-direction:column}}.wp-block-ponyo-callie a.wp-block-ponyo-button{justify-content:center;margin-bottom:0;max-width:none}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/callie/callie-style.css \*/

.wp-block-navigation .wp-block-navigation-item\_\_label{overflow-wrap:break-word}.wp-block-navigation .wp-block-navigation-item\_\_description{display:none}.link-ui-tools{outline:1px solid #f0f0f0;padding:8px}.link-ui-block-inserter{padding-top:8px}.link-ui-block-inserter\_\_back{margin-left:8px;text-transform:uppercase}
/\*# sourceURL=https://www.docker.com/wp/wp-includes/blocks/navigation-link/style.min.css \*/

.wp-block-search\_\_button{margin-left:10px;word-break:normal}.wp-block-search\_\_button.has-icon{line-height:0}.wp-block-search\_\_button svg{height:1.25em;min-height:24px;min-width:24px;width:1.25em;fill:currentColor;vertical-align:text-bottom}:where(.wp-block-search\_\_button){border:1px solid #ccc;padding:6px 10px}.wp-block-search\_\_inside-wrapper{display:flex;flex:auto;flex-wrap:nowrap;max-width:100%}.wp-block-search\_\_label{width:100%}.wp-block-search.wp-block-search\_\_button-only .wp-block-search\_\_button{box-sizing:border-box;display:flex;flex-shrink:0;justify-content:center;margin-left:0;max-width:100%}.wp-block-search.wp-block-search\_\_button-only .wp-block-search\_\_inside-wrapper{min-width:0!important;transition-property:width}.wp-block-search.wp-block-search\_\_button-only .wp-block-search\_\_input{flex-basis:100%;transition-duration:.3s}.wp-block-search.wp-block-search\_\_button-only.wp-block-search\_\_searchfield-hidden,.wp-block-search.wp-block-search\_\_button-only.wp-block-search\_\_searchfield-hidden .wp-block-search\_\_inside-wrapper{overflow:hidden}.wp-block-search.wp-block-search\_\_button-only.wp-block-search\_\_searchfield-hidden .wp-block-search\_\_input{border-left-width:0!important;border-right-width:0!important;flex-basis:0;flex-grow:0;margin:0;min-width:0!important;padding-left:0!important;padding-right:0!important;width:0!important}:where(.wp-block-search\_\_input){appearance:none;border:1px solid #949494;flex-grow:1;font-family:inherit;font-size:inherit;font-style:inherit;font-weight:inherit;letter-spacing:inherit;line-height:inherit;margin-left:0;margin-right:0;min-width:3rem;padding:8px;text-decoration:unset!important;text-transform:inherit}:where(.wp-block-search\_\_button-inside .wp-block-search\_\_inside-wrapper){background-color:#fff;border:1px solid #949494;box-sizing:border-box;padding:4px}:where(.wp-block-search\_\_button-inside .wp-block-search\_\_inside-wrapper) .wp-block-search\_\_input{border:none;border-radius:0;padding:0 4px}:where(.wp-block-search\_\_button-inside .wp-block-search\_\_inside-wrapper) .wp-block-search\_\_input:focus{outline:none}:where(.wp-block-search\_\_button-inside .wp-block-search\_\_inside-wrapper) :where(.wp-block-search\_\_button){padding:4px 8px}.wp-block-search.aligncenter .wp-block-search\_\_inside-wrapper{margin:auto}.wp-block[data-align=right] .wp-block-search.wp-block-search\_\_button-only .wp-block-search\_\_inside-wrapper{float:right}
/\*# sourceURL=https://www.docker.com/wp/wp-includes/blocks/search/style.min.css \*/

.wp-block-group{box-sizing:border-box}:where(.wp-block-group.wp-block-group-is-layout-constrained){position:relative}
/\*# sourceURL=https://www.docker.com/wp/wp-includes/blocks/group/style.min.css \*/

.wp-block-ponyo-text{color:var(--copyColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.125rem;font-weight:400;letter-spacing:-.225px;line-height:140%;max-width:72ch}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/atoms/text/text-style.css \*/

.wp-block-ponyo-blog-header{margin-bottom:2.5rem;padding-top:2.5rem}.wp-block-ponyo-blog-header .wp-block-ponyo-eyebrow{margin-bottom:1.25rem}.wp-block-ponyo-blog-header .wp-block-ponyo-heading{color:var(--headlineColor);margin-bottom:1.25rem}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/blog/blog-header/blog-header-style.css \*/

.wp-block-ponyo-blog-author{display:flex;flex-direction:column;gap:.75rem;padding-bottom:1rem}.wp-block-ponyo-blog-author .author{align-items:center;display:flex;flex-direction:row;gap:.75rem;padding-top:0;width:100%}.wp-block-ponyo-blog-author .author img{border-radius:50%}.wp-block-ponyo-blog-author .author p{font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.125rem;font-weight:400;letter-spacing:-.225px;line-height:140%;max-width:72ch}.wp-block-ponyo-blog-author .author a{text-decoration:none}.wp-block-ponyo-blog-author .author a:active,.wp-block-ponyo-blog-author .author a:focus,.wp-block-ponyo-blog-author .author a:hover{text-decoration:underline}div.wp-block-ponyo-blog-contributor{display:flex;flex-direction:row;flex-wrap:wrap;font-family:Inter,Helvetica,Arial,sans-serif;font-size:1rem;font-weight:400;font-weight:500;letter-spacing:-.2px;line-height:140%;max-width:72ch}div.wp-block-ponyo-blog-contributor .contributor-headshots{display:flex;z-index:1}div.wp-block-ponyo-blog-contributor .headshot{background-color:var(--backgroundColor);border-radius:100px;margin:auto;overflow:hidden;padding:2px;pointer-events:none;-webkit-user-select:none;-moz-user-select:none;user-select:none}div.wp-block-ponyo-blog-contributor .headshot:first-of-type{border-color:transparent;margin-left:-2px}div.wp-block-ponyo-blog-contributor .headshot:nth-child(n+2){margin-left:-12px}div.wp-block-ponyo-blog-contributor .headshot img{border-radius:100px;height:2rem;width:2rem}div.wp-block-ponyo-blog-contributor .headshot--more>\*{align-content:center;background-color:var(--headlineColor);color:var(--backgroundColor);text-align:center}div.wp-block-ponyo-blog-contributor .contributor-names{align-content:baseline;align-content:center;color:var(--copyColor);flex:1;font-weight:400;min-width:20ch}.carlos-style\_\_featured div.wp-block-ponyo-blog-contributor .contributor-names{min-width:40ch}div.wp-block-ponyo-blog-contributor .contributor-names .contributor{display:inline;font-weight:revert;font-weight:500}div.wp-block-ponyo-blog-contributor .contributor-names a.contributor{color:var(--linkColor)}div.wp-block-ponyo-blog-contributor .contributor-names .others{display:inline-block}div.wp-block-ponyo-blog-contributor .contributor-about{font-weight:400}div.wp-block-ponyo-blog-contributor .contributor-about .content{display:flex;flex-direction:column}div.wp-block-ponyo-blog-contributor .contributor-about .title{color:var(--copyColor2)}div.wp-block-ponyo-blog-contributor .contributor-full{color:var(--copyColor2);display:flex;margin-bottom:1.5rem}div.wp-block-ponyo-blog-contributor .contributor-full:last-of-type{margin-bottom:0}div.wp-block-ponyo-blog-contributor .contributor-full .content{display:flex;flex-direction:column;font-weight:400;margin-top:.25rem}div.wp-block-ponyo-blog-contributor .contributor-full .headshot{margin-left:0;margin-right:1rem}div.wp-block-ponyo-blog-contributor.display\_\_about{flex-direction:column;font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.125rem;font-weight:400;gap:0;letter-spacing:-.225px;line-height:140%;max-width:72ch;padding-top:3rem}div.wp-block-ponyo-blog-contributor.display\_\_about .contributor-full{gap:1rem;margin-bottom:1.75rem}div.wp-block-ponyo-blog-contributor.display\_\_about .contributor-full:last-child{margin-bottom:0}div.wp-block-ponyo-blog-contributor.display\_\_about .headshot{flex-shrink:0;margin:0;padding:0}div.wp-block-ponyo-blog-contributor.display\_\_about .content{margin-top:0;padding-top:.25rem}div.wp-block-ponyo-blog-contributor.display\_\_about .top{align-items:center;display:flex;gap:.5rem}div.wp-block-ponyo-blog-contributor.display\_\_about a.contributor{font-weight:700}div.wp-block-ponyo-blog-contributor.display\_\_about p{font-family:Inter,Helvetica,Arial,sans-serif;font-size:.875rem;font-weight:400;letter-spacing:-.15px;line-height:130%;margin-top:.25rem;max-width:72ch}.single-newsletter .wp-block-ponyo-blog-contributor{margin-top:1.5rem}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/blog/blog-author/blog-author-style.css \*/

.is-small-text{font-size:.875em}.is-regular-text{font-size:1em}.is-large-text{font-size:2.25em}.is-larger-text{font-size:3em}.has-drop-cap:not(:focus):first-letter{float:left;font-size:8.4em;font-style:normal;font-weight:100;line-height:.68;margin:.05em .1em 0 0;text-transform:uppercase}body.rtl .has-drop-cap:not(:focus):first-letter{float:none;margin-left:.1em}p.has-drop-cap.has-background{overflow:hidden}:root :where(p.has-background){padding:1.25em 2.375em}:where(p.has-text-color:not(.has-link-color)) a{color:inherit}p.has-text-align-left[style\*="writing-mode:vertical-lr"],p.has-text-align-right[style\*="writing-mode:vertical-rl"]{rotate:180deg}
/\*# sourceURL=https://www.docker.com/wp/wp-includes/blocks/paragraph/style.min.css \*/

h1:where(.wp-block-heading).has-background,h2:where(.wp-block-heading).has-background,h3:where(.wp-block-heading).has-background,h4:where(.wp-block-heading).has-background,h5:where(.wp-block-heading).has-background,h6:where(.wp-block-heading).has-background{padding:1.25em 2.375em}h1.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h1.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h2.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h2.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h3.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h3.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h4.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h4.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h5.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h5.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]),h6.has-text-align-left[style\*=writing-mode]:where([style\*=vertical-lr]),h6.has-text-align-right[style\*=writing-mode]:where([style\*=vertical-rl]){rotate:180deg}
/\*# sourceURL=https://www.docker.com/wp/wp-includes/blocks/heading/style.min.css \*/

.wp-block-post-content{display:flow-root}
/\*# sourceURL=https://www.docker.com/wp/wp-includes/blocks/post-content/style.min.css \*/

.wp-block-ponyo-blog-author-about{align-items:center;background:var(--backgroundColor);border-bottom:1px solid var(--borderColor);border-left:1px solid var(--borderColor);border-right:1px solid var(--borderColor);box-sizing:border-box;display:flex;flex-direction:column;padding:3rem 2.5rem;width:100%}.wp-block-ponyo-blog-author-about .container .organism,.wp-block-ponyo-blog-author-about .organism{align-items:flex-start;border:none;padding:0 0 1.5rem;width:100%}.wp-block-ponyo-blog-author-about .container .organism:last-child,.wp-block-ponyo-blog-author-about .organism:last-child{padding:0}.wp-block-ponyo-blog-author-about{padding-bottom:0;padding-left:0;padding-right:0}.wp-block-ponyo-blog-author-about .container{width:100%}.wp-block-ponyo-blog-author-about .wp-block-ponyo-heading{color:var(--headlineColor);margin-bottom:2rem}.wp-block-ponyo-blog-author-about .taxonomy{display:flex;flex-wrap:wrap;gap:1.25rem;margin-bottom:1.75rem;margin-top:1.75rem;padding-left:2.5rem}.wp-block-ponyo-blog-author-about .taxonomy a{color:var(--copyColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.125rem;font-weight:400;letter-spacing:-.225px;line-height:140%;max-width:72ch;text-decoration:none}.wp-block-ponyo-blog-author-about .taxonomy a:active,.wp-block-ponyo-blog-author-about .taxonomy a:focus,.wp-block-ponyo-blog-author-about .taxonomy a:hover{text-decoration:underline}.wp-block-ponyo-blog-author-about .taxonomy>span{padding-left:1.5rem;position:relative}.wp-block-ponyo-blog-author-about .taxonomy>span:before{background-position:50%;background-repeat:no-repeat;background-size:contain;content:"";height:100%;left:0;opacity:.6;padding-left:1rem;position:absolute}.wp-block-ponyo-blog-author-about .taxonomy>span:before svg path{fill:var(--copyColor)}.wp-block-ponyo-blog-author-about .taxonomy .post-tag:before{background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSI+PHBhdGggc3Ryb2tlPSJ2YXIoLS1pY29uY29sb3IsIGJsYWNrKSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik04IDhoLjAxTTIgNS4ydjQuNDc1YzAgLjQ4OSAwIC43MzMuMDU1Ljk2My4wNS4yMDQuMTMuNC4yNC41NzkuMTIzLjIwMS4yOTYuMzc0LjY0Mi43Mmw3LjY2OSA3LjY2OWMxLjE4OCAxLjE4OCAxLjc4MiAxLjc4MiAyLjQ2NyAyLjAwNGEzIDMgMCAwIDAgMS44NTQgMGMuNjg1LS4yMjIgMS4yOC0uODE2IDIuNDY3LTIuMDA0bDIuMjEyLTIuMjEyYzEuMTg4LTEuMTg4IDEuNzgyLTEuNzgyIDIuMDA0LTIuNDY3YTMgMyAwIDAgMCAwLTEuODU0Yy0uMjIyLS42ODUtLjgxNi0xLjI4LTIuMDA0LTIuNDY3bC03LjY2OS03LjY2OWMtLjM0Ni0uMzQ2LS41MTktLjUxOS0uNzItLjY0MmEyIDIgMCAwIDAtLjU3OC0uMjRDMTAuNDA5IDIgMTAuMTY0IDIgOS42NzUgMkg1LjJjLTEuMTIgMC0xLjY4IDAtMi4xMDguMjE4YTIgMiAwIDAgMC0uODc0Ljg3NEMyIDMuNTIgMiA0LjA4IDIgNS4yTTguNSA4YS41LjUgMCAxIDEtMSAwIC41LjUgMCAwIDEgMSAwIi8+PC9zdmc+)}.wp-block-ponyo-blog-author-about .taxonomy .post-category:before{background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSI+PHBhdGggc3Ryb2tlPSJ2YXIoLS1pY29uY29sb3IsIGJsYWNrKSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0yMSAxMkg5bTEyLTZIOW0xMiAxMkg5bS00LTZhMSAxIDAgMSAxLTIgMCAxIDEgMCAwIDEgMiAwbTAtNmExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDBtMCAxMmExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDAiLz48L3N2Zz4=)}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/blog/blog-author-about/blog-author-about-style.css \*/

@media screen and (min-width:48rem){.container>.wp-block-ponyo-column:nth-child(n+2){border-left:1px solid var(--borderColor)}}.column-container>.wp-block-ponyo-layout-plain,.column-container>[class\*=wp-block-ponyo-layout-]>.container,.wp-block-ponyo-andre>.wp-block-ponyo-layout-plain,.wp-block-ponyo-andre>[class\*=wp-block-ponyo-layout-]>.container,.wp-block-ponyo-layout-plain>.wp-block-ponyo-layout-plain,.wp-block-ponyo-layout-plain>[class\*=wp-block-ponyo-layout-]>.container{border-left:0;border-right:0}.wp-block-ponyo-layout-plain{align-items:center;background:var(--backgroundColor);border-bottom:0;border-left:1px solid var(--borderColor);border-right:1px solid var(--borderColor);box-sizing:border-box;display:flex;flex-direction:column;width:100%}.wp-block-ponyo-column{height:100%}.wp-block-ponyo-column:has(.wp-block-ponyo-victor,.wp-block-ponyo-igor){min-width:100%}.wp-block-ponyo-column>.column-container{height:100%;width:100%}.wp-block-ponyo-column>.column-container>.wp-block-ponyo-button{margin-left:2.5rem}.wp-block-ponyo-column>.column-container>[class\*=wp-block-ponyo-]:not(.wp-block-ponyo-table){border-left:0;border-right:0}.wp-block-ponyo-column>.column-container>[class\*=wp-block-ponyo-]:last-child,.wp-block-ponyo-column>.column-container>[class\*=wp-block-ponyo-]:last-child>.container{border-bottom:0}.wp-block-ponyo-column>.column-container .organism.last-of-type{border-bottom:none}.wp-block-ponyo-column>.column-container :first-child:is(.wp-block-ponyo-gabriel){border-bottom:0}.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper{align-items:center;background:var(--backgroundColor);border-bottom:1px solid var(--borderColor);border-left:1px solid var(--borderColor);border-right:1px solid var(--borderColor);box-sizing:border-box;display:flex;flex-direction:column;padding:3rem 2.5rem;width:100%}.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper .container .organism,.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper .organism{align-items:flex-start;border:none;padding:0 0 1.5rem;width:100%}.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper .container .organism:last-child,.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper .organism:last-child{padding:0}.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper.align\_\_center{text-align:center}.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper .drawer-label-closed.active,.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper .drawer-label-open.active{display:revert}.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper .drawer-label-closed.inactive,.wp-block-ponyo-column.is-drawer .drawer-toggle-wrapper .drawer-label-open.inactive{display:none}.wp-block-ponyo-column.is-drawer .column-container+.drawer-toggle-wrapper{margin-bottom:0;margin-top:1.75rem}.wp-block-ponyo-column.is-drawer .column-container{height:0;overflow:hidden}.wp-block-ponyo-column.is-drawer .wp-block-ponyo-button{-webkit-user-select:none;-moz-user-select:none;user-select:none}.wp-block-ponyo-column>.wp-block-ponyo-image,.wp-block-ponyo-column>.wp-block-ponyo-kevin,.wp-block-ponyo-column>.wp-block-ponyo-video{border-bottom:1px solid var(--borderColor);border-left:1px solid var(--borderColor);border-right:1px solid var(--borderColor);width:calc(100% - 2px)}.column-container>.wp-block-ponyo-carlos{width:100%}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/layouts/column/column-style.css \*/



.wp-block-ponyo-blog-sidebar{display:flex;flex-direction:column;padding-top:0;position:sticky;top:var(--menuHeight,0);width:100%}.wp-block-ponyo-blog-sidebar h4{border-bottom:1px solid var(--borderColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.125rem;font-weight:400;font-weight:500;letter-spacing:-.225px;line-height:140%;margin:2.5rem 0 1.25rem;max-width:72ch;padding:0 2.5rem 1rem}.wp-block-ponyo-blog-sidebar .post-date{margin-bottom:1rem}.wp-block-ponyo-blog-sidebar .post-date p{font-family:Inter,Helvetica,Arial,sans-serif;font-size:1rem;font-weight:400;letter-spacing:-.2px;line-height:140%;max-width:72ch;padding:0 2.5rem}.wp-block-ponyo-blog-sidebar .post-categories a,.wp-block-ponyo-blog-sidebar .post-tags a{color:var(--copyColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:1rem;font-weight:400;letter-spacing:-.2px;line-height:140%;max-width:72ch;text-decoration:none}.wp-block-ponyo-blog-sidebar .post-categories a:active,.wp-block-ponyo-blog-sidebar .post-categories a:focus,.wp-block-ponyo-blog-sidebar .post-categories a:hover,.wp-block-ponyo-blog-sidebar .post-tags a:active,.wp-block-ponyo-blog-sidebar .post-tags a:focus,.wp-block-ponyo-blog-sidebar .post-tags a:hover{text-decoration:underline}.wp-block-ponyo-blog-sidebar .post-categories ul,.wp-block-ponyo-blog-sidebar .post-tags ul{list-style-type:none;padding:0 2.5rem}.wp-block-ponyo-blog-sidebar .post-categories li,.wp-block-ponyo-blog-sidebar .post-tags li{padding-left:1.875rem;position:relative}.wp-block-ponyo-blog-sidebar .post-categories li:before,.wp-block-ponyo-blog-sidebar .post-tags li:before{background-position:50%;background-repeat:no-repeat;background-size:contain;content:"";height:100%;left:0;opacity:.6;position:absolute;width:1rem}.wp-block-ponyo-blog-sidebar .post-categories li:before svg path,.wp-block-ponyo-blog-sidebar .post-tags li:before svg path{fill:var(--copyColor)}.wp-block-ponyo-blog-sidebar .post-tags li:before{background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSI+PHBhdGggc3Ryb2tlPSJ2YXIoLS1pY29uY29sb3IsIGJsYWNrKSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik04IDhoLjAxTTIgNS4ydjQuNDc1YzAgLjQ4OSAwIC43MzMuMDU1Ljk2My4wNS4yMDQuMTMuNC4yNC41NzkuMTIzLjIwMS4yOTYuMzc0LjY0Mi43Mmw3LjY2OSA3LjY2OWMxLjE4OCAxLjE4OCAxLjc4MiAxLjc4MiAyLjQ2NyAyLjAwNGEzIDMgMCAwIDAgMS44NTQgMGMuNjg1LS4yMjIgMS4yOC0uODE2IDIuNDY3LTIuMDA0bDIuMjEyLTIuMjEyYzEuMTg4LTEuMTg4IDEuNzgyLTEuNzgyIDIuMDA0LTIuNDY3YTMgMyAwIDAgMCAwLTEuODU0Yy0uMjIyLS42ODUtLjgxNi0xLjI4LTIuMDA0LTIuNDY3bC03LjY2OS03LjY2OWMtLjM0Ni0uMzQ2LS41MTktLjUxOS0uNzItLjY0MmEyIDIgMCAwIDAtLjU3OC0uMjRDMTAuNDA5IDIgMTAuMTY0IDIgOS42NzUgMkg1LjJjLTEuMTIgMC0xLjY4IDAtMi4xMDguMjE4YTIgMiAwIDAgMC0uODc0Ljg3NEMyIDMuNTIgMiA0LjA4IDIgNS4yTTguNSA4YS41LjUgMCAxIDEtMSAwIC41LjUgMCAwIDEgMSAwIi8+PC9zdmc+);content:""}.wp-block-ponyo-blog-sidebar .post-categories li:before{background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0ibm9uZSI+PHBhdGggc3Ryb2tlPSJ2YXIoLS1pY29uY29sb3IsIGJsYWNrKSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjIiIGQ9Ik0yMSAxMkg5bTEyLTZIOW0xMiAxMkg5bS00LTZhMSAxIDAgMSAxLTIgMCAxIDEgMCAwIDEgMiAwbTAtNmExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDBtMCAxMmExIDEgMCAxIDEtMiAwIDEgMSAwIDAgMSAyIDAiLz48L3N2Zz4=)}.wp-block-ponyo-blog-sidebar .wp-block-ponyo-john{border-bottom:1px solid var(--borderColor);margin:0;padding:2.5rem}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/blog/blog-sidebar/blog-sidebar-style.css \*/

.wp-block-ponyo-layout-sidebar-right{width:100%}.wp-block-ponyo-layout-sidebar-right>.container{align-items:center;align-items:start;align-items:stretch;background:var(--backgroundColor);border-bottom:1px solid var(--borderColor);border-left:1px solid var(--borderColor);border-right:1px solid var(--borderColor);box-sizing:border-box;display:flex;display:grid;flex-direction:column;grid-template-columns:minmax(0,2.5fr) minmax(0,1fr);width:100%}@media screen and (max-width:47.9375rem){.wp-block-ponyo-layout-sidebar-right>.container{grid-template-columns:100%}}.wp-block-ponyo-layout-sidebar-right .wp-block-ponyo-column{border:0}@media screen and (min-width:48rem){.wp-block-ponyo-layout-sidebar-right .wp-block-ponyo-column:first-of-type{border-right:none}}.wp-block-ponyo-layout-sidebar-right .wp-block-ponyo-column .column-container{width:100%}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/layouts/layout-sidebar-right/layout-sidebar-right-style.css \*/

.wp-block-ponyo-gabriel{background:var(--backgroundColor);border-bottom:1px solid var(--borderColor);border-left:1px solid var(--borderColor);border-right:1px solid var(--borderColor);box-sizing:border-box;display:flex;flex-direction:column;padding:3rem 2.5rem;width:100%}.wp-block-ponyo-gabriel .container .organism,.wp-block-ponyo-gabriel .organism{align-items:flex-start;border:none;padding:0 0 1.5rem;width:100%}.wp-block-ponyo-gabriel .container .organism:last-child,.wp-block-ponyo-gabriel .organism:last-child{padding:0}.wp-block-ponyo-gabriel{align-items:center;height:unset;text-align:center}.wp-block-ponyo-gabriel.text-align\_\_left>.container{align-items:flex-start;text-align:left}.wp-block-ponyo-gabriel>.container{align-items:center;display:flex;flex-direction:column;width:100%}.wp-block-ponyo-gabriel .wp-block-ponyo-logo{height:4rem;padding:0}.wp-block-ponyo-gabriel .wp-block-ponyo-eyebrow{margin-bottom:.75rem}.wp-block-ponyo-gabriel .wp-block-ponyo-heading{color:var(--headlineColor);margin-bottom:.75rem;text-wrap:balance}.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-sm{font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.125rem;font-weight:400;font-weight:500;letter-spacing:-.225px;line-height:140%;max-width:72ch}.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-md{font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.25rem;font-weight:500;letter-spacing:-.25px;line-height:150%;max-width:72ch}.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-lg{font-family:Repro,Helvetica,Arial,sans-serif;font-size:1.5rem;font-weight:500;letter-spacing:-.3px;line-height:120%;max-width:72ch}.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-xl{font-family:Repro,Helvetica,Arial,sans-serif;font-size:2rem;font-weight:500;letter-spacing:-.4px;line-height:120%;max-width:72ch}.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-2xl{font-family:Repro,Helvetica,Arial,sans-serif;font-size:2.5rem;font-weight:500;letter-spacing:-.5px;line-height:120%;max-width:72ch}.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-3xl,.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-4xl,.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-5xl,.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-6xl,.wp-block-ponyo-gabriel .wp-block-ponyo-heading.text-7xl{font-family:Repro,Helvetica,Arial,sans-serif;font-size:3rem;font-weight:500;letter-spacing:-.6px;line-height:120%;max-width:50ch}.wp-block-ponyo-gabriel .wp-block-ponyo-text{color:var(--copyColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.125rem;font-weight:400;font-weight:500;letter-spacing:-.225px;line-height:140%;margin-bottom:.75rem;max-width:72ch;text-wrap:balance}.entry-content .organism .container>.wp-block-ponyo-gabriel{border-left:none;border-right:none}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/gabriel/gabriel-style.css \*/

.wp-block-ponyo-carlos{transition:all .25s ease}.wp-block-ponyo-carlos:active,.wp-block-ponyo-carlos:hover{background:var(--cardBackgroundHover)}.wp-block-ponyo-carlos:active{transform:translateY(-4px)}.wp-block-ponyo-carlos{align-items:start;display:grid;grid-row:span 8;grid-template-rows:subgrid;grid-gap:0;background:var(--cardBackgroundColor);border:1px solid var(--borderColor);overflow:hidden;padding:2rem 3rem;width:calc(100% + 1px)}.wp-block-ponyo-carlos:hover{text-decoration:none}.wp-block-ponyo-carlos.bg\_\_image{background-position:50%;background-size:cover}.wp-block-ponyo-carlos .image-container{display:flex;margin-bottom:2rem;overflow:hidden;pointer-events:none;width:100%}.wp-block-ponyo-carlos img{height:100%;max-width:none;pointer-events:none;width:100%}.wp-block-ponyo-carlos .icon{margin-bottom:1rem}.wp-block-ponyo-carlos .icon svg{height:2.5rem;width:2.5rem}.wp-block-ponyo-carlos .eyebrow{color:var(--copyColor2);display:flex;font-family:Inter,Helvetica,Arial,sans-serif;font-size:.875rem;font-weight:400;font-weight:500;justify-content:space-between;letter-spacing:-.15px;line-height:130%;max-width:72ch}.wp-block-ponyo-carlos .eyebrow:has(\*){margin-bottom:1rem}.wp-block-ponyo-carlos .copy-container{display:flex;flex-direction:column;gap:.5rem}.wp-block-ponyo-carlos .copy-container:not(:last-child){margin-bottom:1rem}.wp-block-ponyo-carlos .wp-block-ponyo-heading{align-items:center;display:flex;gap:.5rem;--iconColor:var(--copyColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:1.125rem;font-weight:400;font-weight:500;letter-spacing:-.225px;line-height:140%;max-width:72ch}.wp-block-ponyo-carlos .wp-block-ponyo-heading svg{height:1.25rem;width:1.25rem}.wp-block-ponyo-carlos .body-copy{color:var(--copyColor);font-size:1rem;letter-spacing:-.2px;line-height:140%}.wp-block-ponyo-carlos .body-copy,.wp-block-ponyo-carlos .footer{font-family:Inter,Helvetica,Arial,sans-serif;font-weight:400;max-width:72ch}.wp-block-ponyo-carlos .footer{color:var(--subheadColor);display:flex;flex-direction:column;font-size:.875rem;gap:.375rem;letter-spacing:-.15px;line-height:130%}.wp-block-ponyo-carlos .footer:has(\*):not(:last-child){margin-bottom:1rem}.wp-block-ponyo-carlos .footer-top{font-weight:500}.wp-block-ponyo-carlos .contributors:has(\*):not(:last-child){margin-bottom:1rem}.wp-block-ponyo-carlos .contributors .wp-block-ponyo-blog-contributor{padding:0}.wp-block-ponyo-carlos .link-copy{align-items:center;align-self:end;color:var(--cardCTATextColor);display:flex;font-family:Inter,Helvetica,Arial,sans-serif;font-size:.875rem;font-weight:400;font-weight:500;letter-spacing:-.15px;line-height:130%;margin-top:1rem;max-width:72ch;transition:all .25s ease}.wp-block-ponyo-carlos .link-copy span{height:1rem;margin:.375rem 0 0 .5rem;width:.5rem}.wp-block-ponyo-carlos.carlos-style\_\_small .image-container{grid-row:2;margin-bottom:1rem}.wp-block-ponyo-carlos.carlos-style\_\_small .image-container img{height:5rem;-o-object-fit:cover;object-fit:cover;width:5rem}.wp-block-ponyo-carlos.carlos-style\_\_small .eyebrow{grid-row:1}.wp-block-ponyo-carlos.carlos-style\_\_small.post-type\_\_contributor img{border-radius:50%}.wp-block-ponyo-carlos.carlos-style\_\_paddingless .image-container{margin-left:-3rem;margin-top:-2rem;width:calc(100% + 6rem)}.wp-block-ponyo-carlos.carlos-style\_\_featured{grid-template-columns:repeat(2,1fr);grid-template-rows:auto 1fr auto auto auto;width:100%;grid-column-gap:1.75rem;border-bottom:none;border-left:none}@media screen and (max-width:31.1875rem){.wp-block-ponyo-carlos.carlos-style\_\_featured{grid-template-columns:1fr}}.wp-block-ponyo-carlos.carlos-style\_\_featured .image-container{grid-row-start:span 5;margin-left:-3rem;margin-top:-2rem;overflow:initial;width:calc(100% + 6rem)}@media screen and (min-width:31.25rem){.wp-block-ponyo-carlos.carlos-style\_\_featured .image-container{margin:0;width:auto}}.wp-block-ponyo-carlos.carlos-style\_\_featured .wp-block-ponyo-heading{font-family:Repro,Helvetica,Arial,sans-serif;font-size:2.5rem;font-weight:500;letter-spacing:-.5px;line-height:120%;max-width:72ch}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/carlos/carlos-style.css \*/

.wp-block-post-template{box-sizing:border-box;list-style:none;margin-bottom:0;margin-top:0;max-width:100%;padding:0}.wp-block-post-template.is-flex-container{display:flex;flex-direction:row;flex-wrap:wrap;gap:1.25em}.wp-block-post-template.is-flex-container>li{margin:0;width:100%}@media (min-width:600px){.wp-block-post-template.is-flex-container.is-flex-container.columns-2>li{width:calc(50% - .625em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-3>li{width:calc(33.33333% - .83333em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-4>li{width:calc(25% - .9375em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-5>li{width:calc(20% - 1em)}.wp-block-post-template.is-flex-container.is-flex-container.columns-6>li{width:calc(16.66667% - 1.04167em)}}@media (max-width:600px){.wp-block-post-template-is-layout-grid.wp-block-post-template-is-layout-grid.wp-block-post-template-is-layout-grid.wp-block-post-template-is-layout-grid{grid-template-columns:1fr}}.wp-block-post-template-is-layout-constrained>li>.alignright,.wp-block-post-template-is-layout-flow>li>.alignright{float:right;margin-inline-end:0;margin-inline-start:2em}.wp-block-post-template-is-layout-constrained>li>.alignleft,.wp-block-post-template-is-layout-flow>li>.alignleft{float:left;margin-inline-end:2em;margin-inline-start:0}.wp-block-post-template-is-layout-constrained>li>.aligncenter,.wp-block-post-template-is-layout-flow>li>.aligncenter{margin-inline-end:auto;margin-inline-start:auto}
/\*# sourceURL=https://www.docker.com/wp/wp-includes/blocks/post-template/style.min.css \*/

.wp-block-ponyo-yolanda{align-items:center;background:var(--backgroundColor);border-bottom:1px solid var(--borderColor);border-left:1px solid var(--borderColor);border-right:1px solid var(--borderColor);box-sizing:border-box;display:flex;flex-direction:column;padding:3rem 2.5rem;width:100%}.wp-block-ponyo-yolanda .container .organism,.wp-block-ponyo-yolanda .organism{align-items:flex-start;border:none;padding:0 0 1.5rem;width:100%}.wp-block-ponyo-yolanda,.wp-block-ponyo-yolanda .container .organism:last-child,.wp-block-ponyo-yolanda .organism:last-child{padding:0}.wp-block-ponyo-yolanda>.container{margin:0 0 -1px -1px;width:calc(100% + 1px)}.wp-block-ponyo-yolanda ul.wp-block-post-template{display:grid;grid-auto-flow:row;grid-template-columns:repeat(auto-fit,minmax(31ch,1fr));width:100%}.wp-block-ponyo-yolanda .wp-block-post{display:grid;grid-row:span 7;grid-template-rows:subgrid;grid-gap:0 1.25rem}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/organisms/yolanda/yolanda-style.css \*/

.wp-block-ponyo-faith{width:-moz-max-content;width:max-content}@media screen and (max-width:61.1875rem){.wp-block-ponyo-faith{flex:1}}.wp-block-ponyo-faith h2{color:var(--headlineColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:.75rem;font-weight:400;font-weight:500;letter-spacing:-.15px;line-height:130%;margin:0 0 .5rem;max-width:72ch}.wp-block-ponyo-faith ul{list-style:none;padding:0}.wp-block-ponyo-faith ul li{margin:0 0 .5rem}.wp-block-ponyo-faith a{color:var(--copyColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:.875rem;font-weight:400;letter-spacing:-.15px;line-height:130%;line-height:1;max-width:72ch;text-decoration:initial}.wp-block-ponyo-faith a:active,.wp-block-ponyo-faith a:focus,.wp-block-ponyo-faith a:hover{text-decoration:underline}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/faith/faith-style.css \*/

.wp-block-ponyo-freddie{padding:0 0 2rem;width:100%}.wp-block-ponyo-freddie .menu-container{flex-direction:column;width:100%}@media screen and (min-width:31.25rem){.wp-block-ponyo-freddie .menu-container{display:flex;flex-direction:row;flex-wrap:wrap;gap:1.75rem;justify-content:space-between}}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/freddie/freddie-style.css \*/

.wp-block-ponyo-newsletter-social ul.social-wrap{display:flex;flex-direction:row;gap:.75rem;list-style-type:none;margin:0 0 2rem;padding:3rem 2.5rem 0}.wp-block-ponyo-newsletter-social ul.social-wrap svg{height:1.5rem;width:1.5rem}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/newsletter/newsletter-social/newsletter-social-style.css \*/

.wp-block-ponyo-foster{align-items:center;display:flex}@media screen and (max-width:47.9375rem){.wp-block-ponyo-foster{align-items:center;flex-direction:column;gap:1.5rem}}.wp-block-ponyo-foster .wp-block-ponyo-text,.wp-block-ponyo-foster a{color:var(--copyColor);font-family:Inter,Helvetica,Arial,sans-serif;font-size:.75rem;font-weight:400;letter-spacing:-.15px;line-height:130%;max-width:72ch}@media screen and (min-width:48rem){.wp-block-ponyo-foster .container{display:flex;flex-wrap:wrap;padding-left:1.25rem}.wp-block-ponyo-foster .container>:not(:first-child):before{background-color:var(--copyColor);content:"";display:inline-block;height:.75rem;margin:0 8px;position:relative;top:2px;width:1px}.wp-block-ponyo-foster #ot-sdk-btn{margin-left:2rem}}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/foster/foster-style.css \*/

.wp-block-ponyo-franklin{align-items:center;display:flex;justify-content:space-between;padding-top:1.25rem;width:100%}@media screen and (max-width:47.9375rem){.wp-block-ponyo-franklin{flex-direction:column;gap:1.5rem}}.wp-block-ponyo-franklin ul.social-wrap{align-items:flex-start;display:flex;flex-direction:row;gap:1.25rem;list-style:none;margin:0;padding:0}.wp-block-ponyo-franklin ul.social-wrap svg{--iconColor:var(--copyColor)}@media screen and (max-width:61.1875rem){.wp-block-ponyo-franklin ul.social-wrap{gap:.75rem}}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/molecules/franklin/franklin-style.css \*/

.wp-block-ponyo-fritz{align-items:center;background:var(--backgroundColor);border-bottom:1px solid var(--borderColor);border-left:1px solid var(--borderColor);border-right:1px solid var(--borderColor);box-sizing:border-box;display:flex;flex-direction:column;padding:3rem 2.5rem;width:100%}.wp-block-ponyo-fritz .container .organism,.wp-block-ponyo-fritz .organism{align-items:flex-start;border:none;padding:0 0 1.5rem;width:100%}.wp-block-ponyo-fritz .container .organism:last-child,.wp-block-ponyo-fritz .organism:last-child{padding:0}.wp-block-ponyo-fritz>.container{width:100%}
/\*# sourceURL=https://www.docker.com/app/themes/Ponyo/dist/blocks/organisms/fritz/fritz-style.css \*/

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

.skip-link.screen-reader-text {
border: 0;
clip-path: inset(50%);
height: 1px;
margin: -1px;
overflow: hidden;
padding: 0;
position: absolute !important;
width: 1px;
word-wrap: normal !important;
}
.skip-link.screen-reader-text:focus {
background-color: #eee;
clip-path: none;
color: #444;
display: block;
font-size: 1em;
height: auto;
left: 5px;
line-height: normal;
padding: 15px 23px 14px;
text-decoration: none;
top: 5px;
width: auto;
z-index: 100000;
}
/\*# sourceURL=wp-block-template-skip-link-inline-css \*/







const dkr\_post\_meta = {"created\_date":"2026-01-06","modified\_date":"2026-01-09","author":"Stan Hamara"};
 
document.documentElement.classList.add('js');



function OptanonWrapper() {}



(function(w, d, s, l, i) {
w[l] = w[l] || [];
w[l].push({
'gtm.start': new Date().getTime(),
event: 'gtm.js'
});
var f = d.getElementsByTagName(s)[0],
j = d.createElement(s),
dl = l != 'dataLayer' ? '&l=' + l : '';
j.async = true;
j.src =
'https://www.googletagmanager.com/gtm.js?id=' + i + dl;
f.parentNode.insertBefore(j, f);
})(window, document, 'script', 'dataLayer', 'GTM-WL2QLG5');



!function(e, a, n, t) {
var i = e.head;
if (i) {
if (a) return;
var o = e.createElement("style");
o.id = "alloy-prehiding", o.innerText = n, i.appendChild(o), setTimeout(function() {
o.parentNode && o.parentNode.removeChild(o)
}, t)
}
}
(document, document.location.href.indexOf("adobe\_authoring\_enabled") !== -1, "body {opacity: 0!important}", 1500);






* AI

  AI

  + [Docker for AI

    Simplifying Agent Development](/solutions/docker-ai/ "/solutions/docker-ai/")
  + [Docker MCP Catalog and Toolkit

    Connect and manage MCP tools](/products/mcp-catalog-and-toolkit/ "/products/mcp-catalog-and-toolkit/")
  + [Docker Model Runner

    Local-first LLM inference made easy](/products/model-runner/ "/products/model-runner/")
  + [Docker Sandboxes
    New

    Isolated environments for coding agents](/products/docker-sandboxes/ "/products/docker-sandboxes/")

  More resources for developers

  [Docker Brings Compose to the Agent Era: Building AI Agents is Now Easy

  Docker Accelerates Agent Development

  Read more](/blog/build-ai-agents-with-docker-compose/ "/blog/build-ai-agents-with-docker-compose/")
* [Products](/products/ "/products/")

  Products

  + [Docker Hardened Images
    New

    Ship with secure, enterprise-ready images](/products/hardened-images/ "/products/hardened-images/")
  + [Docker Desktop

    Containerize your applications](/products/docker-desktop/ "/products/docker-desktop/")
  + [Docker Hub

    Discover and share container images](/products/docker-hub/ "/products/docker-hub/")
  + [Docker Scout

    Simplify the software supply chain](/products/docker-scout/ "/products/docker-scout/")
  + [Docker Build Cloud

    Speed up your image builds](/products/build-cloud/ "/products/build-cloud/")
  + [Testcontainers Desktop
    xml version="1.0" encoding="UTF-8"?

    Local testing with real dependencies](https://testcontainers.com/desktop/ "https://testcontainers.com/desktop/")
  + [Testcontainers Cloud
    xml version="1.0" encoding="UTF-8"?

    Test without limits in the cloud](https://testcontainers.com/cloud/ "https://testcontainers.com/cloud/")
  + [Docker MCP Catalog and Toolkit
    New

    Connect and manage MCP tools](/products/mcp-catalog-and-toolkit/ "/products/mcp-catalog-and-toolkit/")
  + [Docker Offload

    Break free of local constraints](/products/docker-offload/ "/products/docker-offload/")

  [Secure Agent Execution with NanoClaw and Docker Sandboxes

  NanoClaw integrates with Docker Sandboxes to run AI

  Read more](/blog/nanoclaw-docker-sandboxes-agent-security/ "/blog/nanoclaw-docker-sandboxes-agent-security/")
* Developers

  Developers

  + [Documentation
    xml version="1.0" encoding="UTF-8"?

    Find guides for Docker products](https://docs.docker.com/ "https://docs.docker.com/")
  + [Getting Started

    Learn the Docker basics](/get-started/ "/get-started/")
  + [Resources

    Search a library of helpful materials](/resources/ "/resources/")
  + [Training

    Skill up your Docker knowledge](/resources/trainings/ "/resources/trainings/")
  + [Extensions SDK

    Create and share your own extensions](/developers/sdk/ "/developers/sdk/")
  + [Community

    Connect with other Docker developers](/community/ "/community/")
  + [Open Source

    Explore open source projects](/community/open-source/ "/community/open-source/")
  + [Preview Program

    Help shape the future of Docker](/community/get-involved/developer-preview/ "/community/get-involved/developer-preview/")
  + [Customer Stories

    Get inspired with customer stories](/customer-stories/ "/customer-stories/")

  More resources for developers

  [Introducing Docker Model Runner

  A faster, simpler way to run and test AI models locally

  Read more](/blog/introducing-docker-model-runner/ "/blog/introducing-docker-model-runner/")
  [Deliver Quickly. Build Securely. Stay Competitive.

  Meet growing demands for speed and security with integrated, efficient solutions

  Read more](/resources/reducing-every-day-complexities-for-more-efficient-software-development-white-paper/ "/resources/reducing-every-day-complexities-for-more-efficient-software-development-white-paper/")

  [Get the latest Docker news](/newsletter-subscription/ "/newsletter-subscription/")
* [Pricing](/pricing/ "/pricing/")
* [Support](/support/ "/support/")
* [Blog](/blog/ "/blog/")
* [Company](/company/ "/company/")

  Company

  + [About Us

    Let us introduce ourselves](/company/ "/company/")
  + [What is a Container?

    Learn about containerization](/resources/what-container/ "/resources/what-container/")
  + [Why Docker

    Discover what makes us different](/why-docker/ "/why-docker/")
  + [Trust

    Find our customer trust resources](/trust/ "/trust/")
  + [Partners

    Become a Docker partner](/partners/ "/partners/")
  + [Customer Success

    Learn how you can succeed with Docker](/customer-success/ "/customer-success/")
  + [Events

    Attend live and virtual meet ups](/events/ "/events/")
  + [Docker Store
    xml version="1.0" encoding="UTF-8"?

    Gear up with exclusive SWAG](https://stores.kotisdesign.com/docker "https://stores.kotisdesign.com/docker")
  + [Careers

    Apply to join our team](/careers/ "/careers/")
  + [Contact Us

    We’d love to hear from you](/company/contact/ "/company/contact/")

  [Docker Announces SOC 2 Type 2 Attestation & ISO 27001 Certification

  Learn what this means for Docker security and compliance

  Read more](/blog/docker-announces-soc-2-type-2-attestation-iso-27001-certification/ "/blog/docker-announces-soc-2-type-2-attestation-iso-27001-certification/")

Search

[Sign In](https://app.docker.com/login "https://app.docker.com/login")
[Get Started](/get-started/ "/get-started/")

Toggle menu



Deterministic AI Testing with Session Recording in cagent
=========================================================

Posted Jan 6, 2026

[Stan Hamara](https://www.docker.com/contributors/stan-hamara/ "https://www.docker.com/contributors/stan-hamara/")

AI agents introduce a challenge that traditional software doesn’t have: non-determinism. The same prompt can produce different outputs across runs, making reliable testing difficult. Add API costs and latency to the mix, and developer productivity takes a hit.

Session recording in cagent addresses this directly. Record an AI interaction once, replay it indefinitely—with identical results, zero API costs, and millisecond execution times.

How session recording works
---------------------------

cagent implements the [VCR pattern](https://github.com/vcr/vcr "https://github.com/vcr/vcr"), a proven approach for HTTP mocking. During recording, cagent proxies requests to the AI provider, captures the full request/response cycle, and saves it to a YAML “cassette” file. During replay, incoming requests are matched against the recording and served from cache—no network calls required.

Getting started
---------------

Recording a session requires a single flag:

```
cagent run my-agent.yaml --record "What is Docker?"
# creates: cagent-recording-1736089234.yaml

cagent run my-agent.yaml --record="my-test" "Explain containers"
# creates: my-test.yaml
```

Replaying uses the `--fake` flag with the cassette path:

```
cagent exec my-agent.yaml --fake my-test "Explain containers"
```

The replay completes in milliseconds with no API calls.

One implementation detail worth noting: tool call IDs are normalized before matching. OpenAI generates random IDs on each request, which would otherwise break replay. cagent handles this automatically.

Example: CI/CD integration testing
----------------------------------

Consider a code review agent:

```
# code-reviewer.yaml
agents:
  root:
  model: anthropic/claude-sonnet-4-0
  description: Code review assistant
  instruction: |
	  You are an expert code reviewer. Analyze code for best practices,
	  security issues, performance concerns, and readability.
  toolsets:
  - type: filesystem
```

Record the interaction with `--yolo` to auto-approve tool calls:

```
cagent exec code-reviewer.yaml --record="code-review" --yolo \\
  "Review pkg/auth/handler.go for security issues"
```

In CI, replay without API keys or network access:

```
cagent exec code-reviewer.yaml --fake code-review \\
  "Review pkg/auth/handler.go for security issues"
```

Cassettes can be version-controlled alongside test code. When agent instructions change significantly, delete the cassette and re-record to capture the new behaviour.

Other use cases
---------------

**Cost-effective prompt iteration.** Record a single interaction with an expensive model, then iterate on agent configuration against that recording. The first run incurs API costs; subsequent iterations are free.

```
cagent exec ./agent.yaml --record="expensive-test" "Complex task"
for i in {1..100}; do
  cagent exec ./agent-v$i.yaml --fake expensive-test "Complex task"
done
```

**Issue reproduction.** Users can record a session with `--record bug-report` and share the cassette file. Support teams replay the exact interaction locally for debugging.

**Multi-agent systems.** Recording captures the complete delegation graph: root agent decisions, sub-agent tool calls, and inter-agent communication.

Security and provider support
-----------------------------

Cassettes automatically strip sensitive headers (`Authorization`, `X-Api-Key`) before saving, making them safe to commit to version control. The format is human-readable YAML:

```
version: 2
interactions:
  - id: 0
    request:
      method: POST
      url: &lt;https://api.openai.com/v1/chat/completions&gt;
      body: "{...}"
    response:
      status: 200 OK
      body: "data: {...}"
```

Session recording works with all supported providers: OpenAI, Anthropic, Google, Mistral, xAI, and Nebius.

Get started
-----------

Session recording is available now in cagent. To try it:

```
cagent run ./your-agent.yaml --record="my-session" "Your prompt here"
```

For questions, feedback, or feature requests, visit the [cagent repository](https://github.com/docker/cagent "https://github.com/docker/cagent") or join the [GitHub Discussions](https://github.com/docker/cagent/discussions "https://github.com/docker/cagent/discussions").

[Engineering](https://www.docker.com/blog/category/engineering/ "https://www.docker.com/blog/category/engineering/")

Table of contents

Related Posts
-------------

* [Mar 31, 2026

  #### Docker Sandboxes: Run Agents in YOLO Mode, Safely

  Agents have crossed a threshold. Over a quarter of all production code is now AI-authored, and developers who use agents are merging roughly 60% more pull requests. But these gains only come when you let agents run autonomously. And to unlock that, you have to get out of the way. That means letting agents run…

  Eric Jia,

  Srini Sekaran,

  and

  Timir Karia

  Read now](https://www.docker.com/blog/docker-sandboxes-run-agents-in-yolo-mode-safely/ "https://www.docker.com/blog/docker-sandboxes-run-agents-in-yolo-mode-safely/")
* [May 5, 2026

  #### Generate Images Locally with Docker Model Runner and Open WebUI

  Learn how to generate images locally with Docker Model Runner and Open WebUI using a private, OpenAI-compatible workflow on your own machine.

  Ignasi Lopez Luna

  Read now](https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/ "https://www.docker.com/blog/blog-generate-images-locally-dmr-open-webui/")
* [Scanner Integrations
  May 5, 2026

  #### Precision Container Security with Docker and Black Duck

  The complexity of modern containerized applications often leaves developers drowning in a sea of “noise”—vulnerabilities that exist in the file system but pose zero actual risk to the application. The integration between Black Duck and Docker Hardened Images (DHI) provides a definitive answer to this challenge. By combining Docker’s secure-by-default foundations, using VEX (Vulnerability Exploitability eXchange)…

  Jessy McDermott

  and

  Dan Stelzer

  Read now](https://www.docker.com/blog/precision-container-security-with-docker-and-black-duck/ "https://www.docker.com/blog/precision-container-security-with-docker-and-black-duck/")
* [May 1, 2026

  #### A Virtual Agent team at Docker: How the Coding Agent Sandboxes team uses a fleet of agents to ship faster

  Learn how Docker uses a fleet of AI agents in CI to test, triage, and fix code automatically, helping teams ship faster with secure sandboxes.

  Manuel de la Peña

  Read now](https://www.docker.com/blog/a-virtual-agent-team-at-docker-how-the-coding-agent-sandboxes-team-uses-a-fleet-of-agents-to-ship-faster/ "https://www.docker.com/blog/a-virtual-agent-team-at-docker-how-the-coding-agent-sandboxes-team-uses-a-fleet-of-agents-to-ship-faster/")



Products
--------

* [Products Overview](/products/ "/products/")
* [Docker Desktop](/products/docker-desktop/ "/products/docker-desktop/")
* [Docker Hub](/products/docker-hub/ "/products/docker-hub/")
* [Docker Scout](/products/docker-scout/ "/products/docker-scout/")
* [Docker Build Cloud](/products/build-cloud/ "/products/build-cloud/")
* [Testcontainers Desktop](https://testcontainers.com/desktop/ "https://testcontainers.com/desktop/")
* [Testcontainers Cloud](https://testcontainers.com/cloud/ "https://testcontainers.com/cloud/")
* [Docker MCP Catalog and Toolkit](/products/mcp-catalog-and-toolkit/ "/products/mcp-catalog-and-toolkit/")
* [Docker Hardened Images](/products/hardened-images/ "/products/hardened-images/")

Features
--------

* [Command Line Interface](/products/cli/ "/products/cli/")
* [IDE Extensions](/products/ide/ "/products/ide/")
* [Container Runtime](/products/container-runtime/ "/products/container-runtime/")
* [Docker Extensions](/products/extensions/ "/products/extensions/")
* [Trusted Open Source Content](/products/trusted-content/open-source/ "/products/trusted-content/open-source/")
* [Secure Software Supply Chain](/solutions/security/ "/solutions/security/")

Developers
----------

* [Documentation](https://docs.docker.com/ "https://docs.docker.com/")
* [Getting Started](/get-started/ "/get-started/")
* [Trainings](/resources/trainings "/resources/trainings")
* [Extensions SDK](/developers/sdk/ "/developers/sdk/")
* [Community](/community/ "/community/")
* [Open Source](/community/open-source/ "/community/open-source/")
* [Preview Program](/community/get-involved/developer-preview/ "/community/get-involved/developer-preview/")
* [Newsletter](/newsletter-subscription/ "/newsletter-subscription/")

Pricing
-------

* [Personal](/products/personal/ "/products/personal/")
* [Pro](/products/pro/ "/products/pro/")
* [Team](/products/team/ "/products/team/")
* [Business](/products/business/ "/products/business/")
* [Premium Support and TAM](/pricing/premium-support-tam/ "/pricing/premium-support-tam/")
* [Pricing FAQ](/pricing/faq/ "/pricing/faq/")
* [Contact Sales](/pricing/contact-sales/ "/pricing/contact-sales/")

Company
-------

* [About Us](/company/ "/company/")
* [What is a Container](/resources/what-container/ "/resources/what-container/")
* [Blog](/blog/ "/blog/")
* [Why Docker](/why-docker/ "/why-docker/")
* [Trust](/trust/ "/trust/")
* [Customer Success](/customer-success/ "/customer-success/")
* [Partners](/partners/ "/partners/")
* [Events](/events/ "/events/")
* [Docker System Status](http://dockerstatus.com/ "http://dockerstatus.com/")
* [Newsroom](/company/newsroom/ "/company/newsroom/")
* [Swag Store](https://stores.kotisdesign.com/docker "https://stores.kotisdesign.com/docker")
* [Brand Guidelines](/company/newsroom/media-resources/ "/company/newsroom/media-resources/")
* [Trademark Guidelines](/legal/trademark-guidelines/ "/legal/trademark-guidelines/")
* [Careers](/careers/ "/careers/")
* [Contact Us](/company/contact/ "/company/contact/")

Languages
---------

* [English](/ "/")
* [日本語](/ja-jp/ "/ja-jp/")

* [.cls-1{fill:var(--iconColor, #1d63ed);}](http://twitter.com/docker "http://twitter.com/docker")
* [.cls-1{fill:var(--iconColor, #1d63ed);}](https://www.linkedin.com/company/docker "https://www.linkedin.com/company/docker")
* [.cls-1{fill:var(--iconColor, #1d63ed);}](https://www.instagram.com/dockerinc/ "https://www.instagram.com/dockerinc/")
* [.cls-1{fill:var(--iconColor, #1d63ed);}](http://www.youtube.com/user/dockerrun "http://www.youtube.com/user/dockerrun")
* [.cls-1{fill:var(--iconColor, var(--iconColor, #1d63ed));}](https://www.facebook.com/docker.run "https://www.facebook.com/docker.run")
* [.cls-1{fill:var(--iconColor, #1d63ed);}](/blog/feed "/blog/feed")

© 2026 Docker Inc. All rights reserved

[Terms of Service](/legal/docker-terms-service "/legal/docker-terms-service")
[Privacy](/legal/privacy "/legal/privacy")
[Legal](/legal/ "/legal/")

Cookie Settings

{"prefetch":[{"source":"document","where":{"and":[{"href\_matches":"/\*"},{"not":{"href\_matches":["/wp/wp-\*.php","/wp/wp-admin/\*","/app/uploads/\*","/app/\*","/app/plugins/\*","/app/themes/Ponyo/\*","/\*\\?(.+)"]}},{"not":{"selector\_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector\_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}




































(function(){
var corecss = document.createElement('link');
var themecss = document.createElement('link');
var corecssurl = "https://www.docker.com/app/plugins/syntaxhighlighter/syntaxhighlighter3/styles/shCore.css?ver=3.0.9b";
if ( corecss.setAttribute ) {
corecss.setAttribute( "rel", "stylesheet" );
corecss.setAttribute( "type", "text/css" );
corecss.setAttribute( "href", corecssurl );
} else {
corecss.rel = "stylesheet";
corecss.href = corecssurl;
}
document.head.appendChild( corecss );
var themecssurl = "https://www.docker.com/app/plugins/syntaxhighlighter/syntaxhighlighter3/styles/shThemeMidnight.css?ver=3.0.9b";
if ( themecss.setAttribute ) {
themecss.setAttribute( "rel", "stylesheet" );
themecss.setAttribute( "type", "text/css" );
themecss.setAttribute( "href", themecssurl );
} else {
themecss.rel = "stylesheet";
themecss.href = themecssurl;
}
document.head.appendChild( themecss );
})();
SyntaxHighlighter.config.strings.expandSource = '+ expand source';
SyntaxHighlighter.config.strings.help = '?';
SyntaxHighlighter.config.strings.alert = 'SyntaxHighlighter\n\n';
SyntaxHighlighter.config.strings.noBrush = 'Can\'t find brush for: ';
SyntaxHighlighter.config.strings.brushNotHtmlScript = 'Brush wasn\'t configured for html-script option: ';
SyntaxHighlighter.defaults['pad-line-numbers'] = false;
SyntaxHighlighter.defaults['toolbar'] = false;
SyntaxHighlighter.all();
// Infinite scroll support
if ( typeof( jQuery ) !== 'undefined' ) {
jQuery( function( $ ) {
$( document.body ).on( 'post-load', function() {
SyntaxHighlighter.highlight();
} );
} );
}

var Marlin = {"apiKey":"mrl\_a2ck5BUyvtKwLOUe3NgOC769BBKYmlF0","endpoint":"https://marlin-2.docker.com"};
//# sourceURL=ponyo-index-js-extra






( function() {
var skipLinkTarget = document.querySelector( 'main' ),
sibling,
skipLinkTargetID,
skipLink;
// Early exit if a skip-link target can't be located.
if ( ! skipLinkTarget ) {
return;
}
/\*
\* Get the site wrapper.
\* The skip-link will be injected in the beginning of it.
\*/
sibling = document.querySelector( '.wp-site-blocks' );
// Early exit if the root element was not found.
if ( ! sibling ) {
return;
}
// Get the skip-link target's ID, and generate one if it doesn't exist.
skipLinkTargetID = skipLinkTarget.id;
if ( ! skipLinkTargetID ) {
skipLinkTargetID = 'wp--skip-link--target';
skipLinkTarget.id = skipLinkTargetID;
}
// Create the skip link.
skipLink = document.createElement( 'a' );
skipLink.classList.add( 'skip-link', 'screen-reader-text' );
skipLink.id = 'wp-skip-link';
skipLink.href = '#' + skipLinkTargetID;
skipLink.innerText = 'Skip to content';
// Inject the skip link.
sibling.parentElement.insertBefore( skipLink, sibling );
}() );
//# sourceURL=wp-block-template-skip-link-js-after

window.DockerBehaviorRules = window.DockerBehaviorRules || {};window.DockerBehaviorRules.config = {"version":"0.2.0","rules":[{"schema\_version":1,"enabled":true,"event":"click","selector":"body.page-id-71338 button.mktoButton","action":"set\_cookie","scope":{"type":"all"},"cookie":{"name":"dr\_p\_rd","value":"true","days":60,"path":"\/","domain":"","sameSite":"Lax"}},{"schema\_version":1,"enabled":true,"event":"click","selector":".page-id-69676 #dkr\_pp\_card\_team, .page-id-69676 #dkr\_pp\_table\_card\_team","action":"set\_cookie","scope":{"type":"all"},"cookie":{"name":"dr\_p\_dct","value":"true","days":60,"path":"\/","domain":"","sameSite":"Lax"}},{"schema\_version":1,"enabled":true,"event":"click","selector":".page-id-69676 #dkr\_pp\_card\_business","action":"set\_cookie","scope":{"type":"all"},"cookie":{"name":"dr\_p\_drb","value":"true","days":60,"path":"\/","domain":"","sameSite":"Lax"}},{"schema\_version":1,"enabled":true,"event":"click","selector":".page-id-69676 #dkr\_pp\_card\_business\_contact, .page-id-69676 #dkr\_pp\_table\_card\_business","action":"set\_cookie","scope":{"type":"all"},"cookie":{"name":"dr\_p\_cs","value":"true","days":60,"path":"\/","domain":"","sameSite":"Lax"}},{"schema\_version":1,"enabled":true,"event":"click","selector":"body.page-id-71338 a.btn-enterprise","action":"set\_cookie","scope":{"type":"all"},"cookie":{"name":"dr\_p\_te","value":"true","days":60,"path":"\/","domain":"","sameSite":"Lax"}},{"schema\_version":1,"enabled":true,"event":"click","selector":"#dkr\_head\_sign\_in","action":"set\_cookie","scope":{"type":"all"},"cookie":{"name":"dr\_p\_si","value":"true","days":60,"path":"\/","domain":"","sameSite":"Lax"}}]};
//# sourceURL=dbr-runtime-js-before


var gforms\_recaptcha\_recaptcha\_strings = {"site\_key":"6LcGUeoqAAAAAEQQG63wGXQsUtH\_R84IlGi\_2WPS","ajaxurl":"https://www.docker.com/wp/wp-admin/admin-ajax.php","nonce":"fbf6b1c6f1"};
//# sourceURL=gforms\_recaptcha\_recaptcha-js-extra


(function($){grecaptcha.ready(function(){$('.grecaptcha-badge').css('visibility','hidden');});})(jQuery);
//# sourceURL=gforms\_recaptcha\_recaptcha-js-after

window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"NRJS-27f33ade91093c8b2a2","applicationID":"1254123379","transactionName":"NgYEbEpYW0ZQB0MPCw9MJ1tMUFpbHhBSCxQNAhJdFVpUW0cFRA==","queueTime":0,"applicationTime":1044,"atts":"GkEHGgJCSEg=","errorBeacon":"bam.nr-data.net","agent":""}
