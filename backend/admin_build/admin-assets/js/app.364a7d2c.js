(function(e){function t(t){for(var r,a,l=t[0],i=t[1],u=t[2],d=0,b=[];d<l.length;d++)a=l[d],Object.prototype.hasOwnProperty.call(o,a)&&o[a]&&b.push(o[a][0]),o[a]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);s&&s(t);while(b.length)b.shift()();return c.push.apply(c,u||[]),n()}function n(){for(var e,t=0;t<c.length;t++){for(var n=c[t],r=!0,l=1;l<n.length;l++){var i=n[l];0!==o[i]&&(r=!1)}r&&(c.splice(t--,1),e=a(a.s=n[0]))}return e}var r={},o={app:0},c=[];function a(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,a),n.l=!0,n.exports}a.m=e,a.c=r,a.d=function(e,t,n){a.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},a.t=function(e,t){if(1&t&&(e=a(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(a.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)a.d(n,r,function(t){return e[t]}.bind(null,r));return n},a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,"a",t),t},a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},a.p="/";var l=window["webpackJsonp"]=window["webpackJsonp"]||[],i=l.push.bind(l);l.push=t,l=l.slice();for(var u=0;u<l.length;u++)t(l[u]);var s=i;c.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"219d":function(e,t,n){},"2f29":function(e,t,n){"use strict";n("6415")},"38a2":function(e,t,n){},"3a3b":function(e,t,n){"use strict";n("a311")},"3c4b":function(e,t,n){"use strict";n("219d")},"49cd":function(e,t,n){"use strict";n("dac3")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("7a23");function o(e,t,n,o,c,a){var l=Object(r["resolveComponent"])("greendi-bird"),i=Object(r["resolveComponent"])("header-component"),u=Object(r["resolveComponent"])("sidebar-component"),s=Object(r["resolveComponent"])("router-view"),d=Object(r["resolveComponent"])("el-main"),b=Object(r["resolveComponent"])("el-container"),m=Object(r["resolveComponent"])("login-page");return c.easterEggShow?(Object(r["openBlock"])(),Object(r["createBlock"])(l,{key:0})):(Object(r["openBlock"])(),Object(r["createElementBlock"])(r["Fragment"],{key:1},[c.isLoadUserInfo?Object(r["createCommentVNode"])("",!0):(Object(r["openBlock"])(),Object(r["createElementBlock"])(r["Fragment"],{key:0},[c.isUserAuth?(Object(r["openBlock"])(),Object(r["createBlock"])(b,{key:0,class:"is-vertical"},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(i,{class:"header","current-user":c.currentUser,onToggleHeader:a.toggleHeader,onAuthSwitch:a.toggleUserAuth,onEasterEgg:a.easterEgg},null,8,["current-user","onToggleHeader","onAuthSwitch","onEasterEgg"]),Object(r["createVNode"])(b,{class:"content"},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(u,{onChangeCurrentItemMenu:a.changeCurrentItemMenu,isCollapse:c.isCollapse,"current-user":c.currentUser},null,8,["onChangeCurrentItemMenu","isCollapse","current-user"]),Object(r["createVNode"])(d,null,{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(s,{"get-span":a.getSpan,"nice-price":a.nicePrice,"get-language-object":a.getLanguageObject,"get-image":a.getImage,"default-language":c.defaultLanguage,"upload-image":a.uploadImage},null,8,["get-span","nice-price","get-language-object","get-image","default-language","upload-image"])]})),_:1})]})),_:1})]})),_:1})):(Object(r["openBlock"])(),Object(r["createBlock"])(b,{key:1},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(m,{onLogged:a.loggedUser},null,8,["onLogged"])]})),_:1}))],64))],64))}var c=n("53ca"),a=n("ade3"),l=n("1da1"),i=(n("159b"),n("b64b"),n("ac1f"),n("5319"),n("b0c0"),n("96cf"),n("d3b7"),n("25f0"),n("99af"),{key:0,class:"material-symbols-outlined"}),u={key:0,class:"material-symbols-outlined"},s={key:0,class:"material-symbols-outlined"};function d(e,t,n,o,c,a){var l=Object(r["resolveComponent"])("el-icon"),d=Object(r["resolveComponent"])("el-menu-item"),b=Object(r["resolveComponent"])("el-menu"),m=Object(r["resolveComponent"])("el-aside");return Object(r["openBlock"])(),Object(r["createBlock"])(m,{class:"sidebar"},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(b,{"active-text-color":"#ffd04b","background-color":"#545c64",class:"sidebar-menu","default-active":e.activeIndex,"text-color":"#fff",collapse:e.isCollapse,router:!0},{default:Object(r["withCtx"])((function(){return[(Object(r["openBlock"])(!0),Object(r["createElementBlock"])(r["Fragment"],null,Object(r["renderList"])(e.filteredMenu,(function(t){return Object(r["openBlock"])(),Object(r["createBlock"])(Object(r["resolveDynamicComponent"])(t.children?"el-sub-menu":"el-menu-item"),{key:t.id,index:t.id.toString(),onClick:function(n){return e.$emit("change-current-item-menu",t)},route:{name:t.routeName}},{title:Object(r["withCtx"])((function(){return[t.children?(Object(r["openBlock"])(),Object(r["createBlock"])(l,{key:0,size:20,class:"sidebar__icon"},{default:Object(r["withCtx"])((function(){return[t.googleIcon?(Object(r["openBlock"])(),Object(r["createElementBlock"])("div",u,Object(r["toDisplayString"])(t.googleIcon),1)):(Object(r["openBlock"])(),Object(r["createBlock"])(Object(r["resolveDynamicComponent"])(t.icon),{key:1}))]})),_:2},1024)):Object(r["createCommentVNode"])("",!0),Object(r["createElementVNode"])("span",null,Object(r["toDisplayString"])(t.title),1)]})),default:Object(r["withCtx"])((function(){return[t.children?Object(r["createCommentVNode"])("",!0):(Object(r["openBlock"])(),Object(r["createBlock"])(l,{key:0,size:20,class:"sidebar__icon"},{default:Object(r["withCtx"])((function(){return[t.googleIcon?(Object(r["openBlock"])(),Object(r["createElementBlock"])("div",i,Object(r["toDisplayString"])(t.googleIcon),1)):(Object(r["openBlock"])(),Object(r["createBlock"])(Object(r["resolveDynamicComponent"])(t.icon),{key:1}))]})),_:2},1024)),t.children&&t.children.length?(Object(r["openBlock"])(!0),Object(r["createElementBlock"])(r["Fragment"],{key:1},Object(r["renderList"])(t.children,(function(n){return Object(r["openBlock"])(),Object(r["createBlock"])(d,{onClick:function(t){return e.$emit("change-current-item-menu",n)},key:n.id,index:"".concat(t.id,"-").concat(n.id),route:{name:n.routeName}},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(l,{size:20,class:"sidebar__icon"},{default:Object(r["withCtx"])((function(){return[n.googleIcon?(Object(r["openBlock"])(),Object(r["createElementBlock"])("div",s,Object(r["toDisplayString"])(n.googleIcon),1)):(Object(r["openBlock"])(),Object(r["createBlock"])(Object(r["resolveDynamicComponent"])(n.icon),{key:1}))]})),_:2},1024),Object(r["createElementVNode"])("span",null,Object(r["toDisplayString"])(n.title),1)]})),_:2},1032,["onClick","index","route"])})),128)):Object(r["createCommentVNode"])("",!0)]})),_:2},1032,["index","onClick","route"])})),128))]})),_:1},8,["default-active","collapse"])]})),_:1})}var b=n("b85c"),m=(n("7db0"),n("0480")),f=n("8a63"),p=n("bfab"),g=n("8ed3"),j=n("f9ee"),O=n("f592"),h=n("eb00"),v=n("e7de"),C=n("5175"),w=n("4a0c"),k=n("218b"),_=n("6c02"),y=Object(r["defineComponent"])({emits:{"change-current-item-menu":null},props:{isCollapse:Boolean,currentUser:Object},components:{Edit:m["a"],Star:f["a"],Coffee:p["a"],House:g["a"],Notebook:j["a"],Plus:O["a"],Coin:h["a"],List:v["a"],User:C["a"],InfoFilled:w["a"],Document:k["a"]},setup:function(){var e=Object(r["ref"])([{title:"Главная",id:1,icon:"InfoFilled",routeName:"home"},{title:"Категории задач",id:2,googleIcon:"category",routeName:"Categories"},{title:"Задачи",id:3,googleIcon:"task",routeName:"home"},{title:"Группы",id:4,googleIcon:"group",routeName:"home"}]),t=Object(_["c"])(),n=Object(r["computed"])((function(){var n,r=Object(b["a"])(e.value);try{for(r.s();!(n=r.n()).done;){var o=n.value;if(t.name===o.routeName)return o.id.toString();var c=(o.children||[]).find((function(e){return t.name===e.routeName}));if(c)return"".concat(o.id,"-").concat(c.id)}}catch(a){r.e(a)}finally{r.f()}return"0"}));return console.log(n.value),{filteredMenu:e,activeIndex:n}}}),V=(n("49cd"),n("d959")),x=n.n(V);const N=x()(y,[["render",d],["__scopeId","data-v-19dc958e"]]);var B=N,I={class:"login"},E=Object(r["createTextVNode"])("Войти");function U(e,t,n,o,c,a){var l=Object(r["resolveComponent"])("el-input"),i=Object(r["resolveComponent"])("el-form-item"),u=Object(r["resolveComponent"])("el-button"),s=Object(r["resolveComponent"])("el-form");return Object(r["openBlock"])(),Object(r["createElementBlock"])("div",I,[Object(r["createVNode"])(s,{class:"login__form",ref:"loginForm",model:c.loginForm,rules:c.loginRules,"label-width":"200px"},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(i,{label:"Имя пользователя",prop:"username"},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(l,{modelValue:c.loginForm.username,"onUpdate:modelValue":t[0]||(t[0]=function(e){return c.loginForm.username=e})},null,8,["modelValue"])]})),_:1}),Object(r["createVNode"])(i,{label:"Пароль",prop:"password"},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(l,{modelValue:c.loginForm.password,"onUpdate:modelValue":t[1]||(t[1]=function(e){return c.loginForm.password=e}),type:"password"},null,8,["modelValue"])]})),_:1}),Object(r["createVNode"])(i,null,{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(u,{type:"primary",onClick:a.login},{default:Object(r["withCtx"])((function(){return[E]})),_:1},8,["onClick"])]})),_:1})]})),_:1},8,["model","rules"])])}var S=n("bc3a"),L=n.n(S),M=L.a.create({baseURL:"/api/v1/admin",headers:{post:{"Content-Type":"application/json"}}}),T=L.a.create({baseURL:"/api/v1/",headers:{post:{"Content-Type":"application/json"}}}),F={name:"LoginPage",emits:{logged:null},data:function(){return{loginForm:{username:"",password:""},loginRules:{username:[{required:!0,message:"Это поле обязательно",trigger:"blur"}],password:[{required:!0,message:"Это поле обязательно",trigger:"blur"}]}}},methods:{login:function(){var e=this;this.$refs.loginForm.validate(function(){var t=Object(l["a"])(regeneratorRuntime.mark((function t(n){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(!n){t.next=13;break}return t.prev=1,t.next=4,(void 0).post("login/",{username:e.loginForm.username,password:e.loginForm.password});case 4:e.$message.success("Вы успешно авторизовались"),e.$emit("logged"),t.next=11;break;case 8:t.prev=8,t.t0=t["catch"](1),400===t.t0.response.status?e.$message.error(t.t0.response.data.message):e.$message.error("Что-то пошло не так при загрузке дополнений: ".concat(t.t0));case 11:t.next=14;break;case 13:return t.abrupt("return",!1);case 14:case"end":return t.stop()}}),t,null,[[1,8]])})));return function(e){return t.apply(this,arguments)}}())}}};n("bc74");const A=x()(F,[["render",U],["__scopeId","data-v-20ec6f6e"]]);var P=A,D={class:"header__content"};function H(e,t,n,o,c,a){var l=Object(r["resolveComponent"])("my-menu"),i=Object(r["resolveComponent"])("el-icon"),u=Object(r["resolveComponent"])("profile-menu"),s=Object(r["resolveComponent"])("el-header");return Object(r["openBlock"])(),Object(r["createBlock"])(s,{class:"header"},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(i,{class:"header__open-icon",onClick:t[0]||(t[0]=function(t){return e.$emit("toggle-header")})},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(l)]})),_:1}),Object(r["createElementVNode"])("div",D,[Object(r["createElementVNode"])("div",{onClick:t[1]||(t[1]=function(){return a.clickEvent&&a.clickEvent.apply(a,arguments)}),class:"header__logo"}),Object(r["createVNode"])(u,{"current-user":n.currentUser,onIsUserAuth:t[2]||(t[2]=function(t){return e.$emit("auth-switch",t)})},null,8,["current-user"])])]})),_:1})}var R=n("0ebb"),$=function(e){return Object(r["pushScopeId"])("data-v-0a11e646"),e=e(),Object(r["popScopeId"])(),e},G={class:"el-dropdown-link"},J={class:"header__user-profile"},q={class:"header__user-avatar"},z=["src"],Q={class:"header__user-info"},K={class:"header__user-name"},W={class:"header__user-group"},X=$((function(){return Object(r["createElementVNode"])("span",{class:"material-symbols-outlined"},"exit_to_app",-1)})),Y=Object(r["createTextVNode"])(" Выйти ");function Z(e,t,n,o,c,a){var l=Object(r["resolveComponent"])("el-dropdown-item"),i=Object(r["resolveComponent"])("el-dropdown-menu"),u=Object(r["resolveComponent"])("el-dropdown");return Object(r["openBlock"])(),Object(r["createBlock"])(u,{placement:"bottom-end",trigger:"click"},{dropdown:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(i,null,{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(l,{class:"header__user-menu-element"},{default:Object(r["withCtx"])((function(){return[X,Y]})),_:1})]})),_:1})]})),default:Object(r["withCtx"])((function(){return[Object(r["createElementVNode"])("span",G,[Object(r["createElementVNode"])("div",J,[Object(r["createElementVNode"])("div",q,[Object(r["createElementVNode"])("img",{src:e.$serverHost+(null!==n.currentUser.avatar?n.currentUser.avatar:"media/avatars/default.jpg"),alt:"Аватар"},null,8,z)]),Object(r["createElementVNode"])("div",Q,[Object(r["createElementVNode"])("h2",K,Object(r["toDisplayString"])(n.currentUser.full_name),1),Object(r["createElementVNode"])("small",W,Object(r["toDisplayString"])(n.currentUser.position),1)])])])]})),_:1})}var ee={name:"Profile",emits:{"is-user-auth":null},props:{currentUser:Object},data:function(){return{isUserAuth:!0}}};n("eeee");const te=x()(ee,[["render",Z],["__scopeId","data-v-0a11e646"]]);var ne=te,re={name:"Header",emits:{"auth-switch":null,"toggle-header":null,"easter-egg":null},components:{myMenu:R["a"],ProfileMenu:ne},props:{currentUser:Object},data:function(){return{clickCounter:0,timeStart:null}},methods:{clickEvent:function(){var e=this;this.timeStart=(new Date).getTime(),this.clickCounter+=1,setTimeout((function(){e.timeStart&&e.timeStart<=(new Date).getTime()-600&&(11===e.clickCounter&&e.$emit("easter-egg"),e.clickCounter=0)}),600)}}};n("3c4b");const oe=x()(re,[["render",H],["__scopeId","data-v-429f03d8"]]);var ce=oe,ae=function(e){return Object(r["pushScopeId"])("data-v-0848b5cc"),e=e(),Object(r["popScopeId"])(),e},le={class:"body"},ie=ae((function(){return Object(r["createElementVNode"])("header",null,[Object(r["createElementVNode"])("h1",null,"Greendi Bird"),Object(r["createElementVNode"])("div",{class:"score-container"},[Object(r["createElementVNode"])("div",{id:"bestScore"}),Object(r["createElementVNode"])("div",{id:"currentScore"})])],-1)})),ue=ae((function(){return Object(r["createElementVNode"])("canvas",{id:"canvas",width:"431",height:"768"},null,-1)})),se=[ie,ue];function de(e,t,n,o,c,a){return Object(r["openBlock"])(),Object(r["createElementBlock"])("div",le,se)}var be=n("2909"),me=(n("d81d"),n("cb29"),n("fb6a"),{name:"GreendiBird",mounted:function(){var e=document.getElementById("canvas"),t=e.getContext("2d"),n=new Image;n.src="https://i.ibb.co/Q9yv5Jk/flappy-bird-set.png";var r,o,c,a,l=!1,i=.2,u=2.2,s=[51,36],d=-7.5,b=e.width/10,m=0,f=0,p=78,g=270,j=function(){return Math.random()*(e.height-(g+p)-p)+p},O=function(){c=0,r=d,o=e.height/2-s[1]/2,a=Array(3).fill().map((function(t,n){return[e.width+n*(g+p),j()]}))},h=function d(){m++,t.drawImage(n,0,0,e.width,e.height,-m*(u/2)%e.width+e.width,0,e.width,e.height),t.drawImage(n,0,0,e.width,e.height,-m*(u/2)%e.width,0,e.width,e.height),l&&a.map((function(r){r[0]-=u,t.drawImage(n,432,588-r[1],p,r[1],r[0],0,p,r[1]),t.drawImage(n,432+p,108,p,e.height-r[1]+g,r[0],r[1]+g,p,e.height-r[1]+g),r[0]<=-p&&(c++,f=Math.max(f,c),a=[].concat(Object(be["a"])(a.slice(1)),[[a[a.length-1][0]+g+p,j()]]),console.log(a)),[r[0]<=b+s[0],r[0]+p>=b,r[1]>o||r[1]+g<o+s[1]].every((function(e){return e}))&&(l=!1,O())})),l?(t.drawImage.apply(t,[n,432,Math.floor(m%9/3)*s[1]].concat(s,[b,o],s)),r+=i,o=Math.min(o+r,e.height-s[1])):(t.drawImage.apply(t,[n,432,Math.floor(m%9/3)*s[1]].concat(s,[e.width/2-s[0]/2,o],s)),o=e.height/2-s[1]/2,t.fillText("Best score : ".concat(f),85,245),t.fillText("Click to play",90,535),t.font="bold 30px courier"),document.getElementById("bestScore").innerHTML="Best : ".concat(f),document.getElementById("currentScore").innerHTML="Current : ".concat(c),window.requestAnimationFrame(d)};O(),n.onload=h,document.addEventListener("click",(function(){return l=!0})),window.onclick=function(){return r=d}}});n("7295"),n("5904");const fe=x()(me,[["render",de],["__scopeId","data-v-0848b5cc"]]);var pe=fe,ge={name:"Admin",data:function(){return{isCollapse:!1,currentItemMenu:{},currentUser:{},isUserAuth:!1,isLoadUserInfo:!0,defaultLanguage:"ru",easterEggShow:!1}},components:{SidebarComponent:B,HeaderComponent:ce,GreendiBird:pe,LoginPage:P},emits:["auth-switch"],created:function(){this.checkLogin()},provide:function(){return{replaceHTML:this.replaceHTML}},methods:{toggleUserAuth:function(e){this.isUserAuth=e},toggleHeader:function(){this.isCollapse=!this.isCollapse},changeCurrentItemMenu:function(e){this.currentItemMenu=e},getSpan:function(e){return Math.ceil(24/e)},checkLogin:function(){var e=this;return Object(l["a"])(regeneratorRuntime.mark((function t(){var n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,T.get("users/current/");case 3:n=t.sent,e.isUserAuth=200===n.status&&!n.data.errors,e.currentUser=null===n||void 0===n?void 0:n.data.user,e.isLoadUserInfo=!1,t.next=13;break;case 9:t.prev=9,t.t0=t["catch"](0),e.isUserAuth=!1,e.isLoadUserInfo=!1;case 13:case"end":return t.stop()}}),t,null,[[0,9]])})))()},loggedUser:function(){this.isUserAuth=!0},nicePrice:function(e){return new Intl.NumberFormat("ru").format(e)},getLanguageObject:function(e,t){var n={},r={};try{return t.forEach((function(t){Object.keys(e[t]).forEach((function(e){return Object.assign(r,Object(a["a"])({},e,null))})),n[t]=r,r={}})),n}catch(o){return console.error(o),{}}},replaceHTML:function(e){if(e&&e.length)return e.replace(/<.*?>/g,"")},getImage:function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"image",n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:this.$host;return null===e[t]?null:"object"===Object(c["a"])(e[t])?e[t].base_64:n+e[t]},uploadImage:function(e){var t=e.file,n=e.element,r=e.fieldName;n[r]={filename:t.name};var o=new FileReader;o.onloadend=function(){n[r].base_64=o.result},o.readAsDataURL(t)},easterEgg:function(){this.easterEggShow=!0}}};n("2f29");const je=x()(ge,[["render",o]]);var Oe=je,he=n("1250");n("7437");function ve(e,t,n,o,c,a){return Object(r["openBlock"])(),Object(r["createElementBlock"])("h1",null,"Code skills admin panel")}var Ce={name:"GreenhousePage",data:function(){return{baseJson:{}}}};n("bf85"),n("3a3b");const we=x()(Ce,[["render",ve],["__scopeId","data-v-09563e20"]]);var ke=we,_e=Object(r["createTextVNode"])(" Сохранить "),ye=Object(r["createTextVNode"])(" Добавить ");function Ve(e,t,n,o,c,a){var l=Object(r["resolveComponent"])("el-input"),i=Object(r["resolveComponent"])("el-table-column"),u=Object(r["resolveComponent"])("el-checkbox"),s=Object(r["resolveComponent"])("el-table"),d=Object(r["resolveComponent"])("el-button"),b=Object(r["resolveComponent"])("el-col"),m=Object(r["resolveComponent"])("el-row"),f=Object(r["resolveComponent"])("el-affix"),p=Object(r["resolveComponent"])("el-scrollbar");return Object(r["openBlock"])(),Object(r["createBlock"])(p,{height:"calc(100vh - 100px)",class:"scrollbar"},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(s,{data:c.categories,style:{width:"100%"}},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(i,{prop:"date",label:"Название"},{default:Object(r["withCtx"])((function(e){return[Object(r["createVNode"])(l,{modelValue:e.row.title,"onUpdate:modelValue":function(t){return e.row.title=t},placeholder:"Название"},null,8,["modelValue","onUpdate:modelValue"])]})),_:1}),Object(r["createVNode"])(i,{prop:"date",label:"Slug (ЧПУ)"},{default:Object(r["withCtx"])((function(e){return[Object(r["createVNode"])(l,{modelValue:e.row.slug,"onUpdate:modelValue":function(t){return e.row.slug=t},placeholder:"Slug"},null,8,["modelValue","onUpdate:modelValue"])]})),_:1}),Object(r["createVNode"])(i,{prop:"date",label:"Активность"},{default:Object(r["withCtx"])((function(e){return[Object(r["createVNode"])(u,{label:"Показывать",modelValue:e.row.active,"onUpdate:modelValue":function(t){return e.row.active=t}},null,8,["modelValue","onUpdate:modelValue"])]})),_:1})]})),_:1},8,["data"]),Object(r["createVNode"])(f,{position:"bottom",offset:20},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(m,{gutter:24},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(b,{span:3},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(d,{onClick:a.saveCategories,class:"button button_save button_full-width",type:"success"},{default:Object(r["withCtx"])((function(){return[_e]})),_:1},8,["onClick"])]})),_:1}),Object(r["createVNode"])(b,{span:3},{default:Object(r["withCtx"])((function(){return[Object(r["createVNode"])(d,{onClick:a.addCategories,class:"button button_add button_full-width",type:"primary"},{default:Object(r["withCtx"])((function(){return[ye]})),_:1},8,["onClick"])]})),_:1})]})),_:1})]})),_:1})]})),_:1})}var xe=n("4995"),Ne={name:"Categories",data:function(){return{categories:null}},created:function(){this.getCategories()},methods:{getCategories:function(){var e=this;return Object(l["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,M.get("categories/").then((function(e){var t=e.data;return t.categories||[]}));case 2:e.categories=t.sent;case 3:case"end":return t.stop()}}),t)})))()},saveCategories:function(){var e=this;return Object(l["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.prev=0,t.next=3,M.post("categories/",{categories:e.categories});case 3:Object(xe["a"])({message:"Успешно сохранено",type:"success"}),t.next=10;break;case 6:t.prev=6,t.t0=t["catch"](0),console.error(t.t0),Object(xe["a"])({message:"Ошибка сохранения ".concat(t.t0),type:"error"});case 10:case"end":return t.stop()}}),t,null,[[0,6]])})))()},addCategories:function(){this.categories.push({id:0,title:null,slug:null,active:!1})}}};const Be=x()(Ne,[["render",Ve]]);var Ie=Be,Ee=[{path:"/",name:"home",component:ke,meta:{title:"Админка"}},{path:"/categories",name:"Categories",component:Ie,meta:{title:"Категории задач"}}],Ue=Object(_["a"])({history:Object(_["b"])("admin"),routes:Ee});Ue.beforeEach((function(e){Object(r["nextTick"])((function(){var t;document.title=(null===(t=e.meta)||void 0===t?void 0:t.title)||"Админка"}))}));var Se=Ue,Le=Object(r["createApp"])(Oe);Le.config.globalProperties.$host="/",Le.config.globalProperties.$serverHost="/",Le.directive("focus",{mounted:function(e){e.focus()}}),Le.use(he["a"]).use(Se).mount("#app")},5904:function(e,t,n){"use strict";n("cdf97")},6415:function(e,t,n){},7295:function(e,t,n){"use strict";n("38a2")},a311:function(e,t,n){},bc74:function(e,t,n){"use strict";n("bfdd")},bf85:function(e,t,n){"use strict";n("ee0a")},bfdd:function(e,t,n){},cdf97:function(e,t,n){},dac3:function(e,t,n){},ee0a:function(e,t,n){},eeee:function(e,t,n){"use strict";n("fb27")},fb27:function(e,t,n){}});
//# sourceMappingURL=app.364a7d2c.js.map