/*
  Como hacer para variar de light a dark theme
*/

/* Esta técnica es buenisima para alternar los themes
Definimos de cada elemento las propiedades que queremos y
agregá antes de todo un nombre yo en este caso usé dark*/

.dark  { background-color: #000!important; color: cyan;}
.dark a { color: cyan;}
.dark input { background-color: #000!important; color: white!important; }
.dark select { background-color: #000!important; color: white!important; }
.dark textarea { background-color: #000!important; color: white!important; }
.dark #page-content-wrapper { background-color: #000!important; color: white!important; }
.dark .card-body { background-color: #000!important; color: white!important; }
.dark #navbar { background-color: #000!important; color: white!important; }
.dark #navbar .dropdown {list-style: none; background-color: black; display: inline-block;}
.dark #navbar .dropdown .nav-link {color:#fff; text-decoration: none;}
.dark #navbar .dropdown .dropdown-menu {color: #fff; background-color: black; text-decoration: none;}
.dark #navbar .dropdown .dropdown-menu .dropdown-divider{ border-color: cyan; }
.dark #navbar .dropdown .dropdown-menu a{color: #fff; background-color: black; text-decoration: none;}
.dark #navbar .dropdown .btn {background: black; color:#fff;}
.dark #navbar .dropdown .btn:hover {background: cyan; color:#000!important;}
.dark #navbar .dropdown .btn:active {background: cyan; color:#000!important;}
.dark #navbar .dropdown .btn:focus {background: cyan; color:#000!important;}
.dark #navbar .dropdown-menu .dropdown-item {display: inline-block;  width: 100%;}
.dark #navbar .dropdown-menu .dropdown-item:hover { background: cyan; color: #000!important; display: inline-block;  width: 100%;}
.dark #navbar .container .dropdown .dropdown-menu a:hover { color: #fff; background-color: #b91773; border-color: #fff; }
.dark footer { background-color: #000!important; color: white!important; }

/* 
Después de esto sólo tenés que asignar al elemento "html" esta clase, yo lo hice con jQuery, y toda
la página va a heredar el estilo anteriormente declarado pisando el anterior:

toggleClass funciona de tal forma que cada vez que la llaman agrega o quita la clase.
Así: $("html").toggleClass("dark"); */
