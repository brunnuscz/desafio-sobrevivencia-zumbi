<template>
  <div id="app" >
      <nav class="navbar navbar-expand navbar-color p-3">
        <div class="collapse navbar-collapse" id="navbar">
          <a class="navbar-brand" href="/index">
            <img src="../public/zombie.png" alt="Zombie">
          </a>
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link to="/index" class="nav-link">Página Inicial</router-link>
            </li>

            <li class="nav-item">
              <router-link to="/list/survivors/" class="nav-link">Sobreviventes</router-link>
            </li>

            <li class="nav-item">
              <router-link to="/index" class="nav-link">Inventário</router-link>
            </li>
          </ul>
        </div>
      </nav>
      <router-view />
  </div>
</template>