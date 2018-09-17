import Sidebar from './SideBar.vue'

const SidebarStore = {
  showSidebar: false,
  sidebarLinks: [
    {
      name: 'Dashboard',
      icon: 'ti-panel',
      path: '/admin/home'
    },
    {
      name: 'Market',
      icon: 'ti-view-list-alt',
      path: '/admin/market'
    },
    {
      name: 'Buy Computation',
      icon: 'ti-user',
      path: '/admin/buy'
    },
    {
      name: 'Rent computations',
      icon: 'ti-bell',
      path: '/admin/rent'
    }
  ],
  displaySidebar (value) {
    this.showSidebar = value
  }
}

const SidebarPlugin = {

  install (Vue) {
    Vue.mixin({
      data () {
        return {
          sidebarStore: SidebarStore
        }
      }
    })

    Object.defineProperty(Vue.prototype, '$sidebar', {
      get () {
        return this.$root.sidebarStore
      }
    })
    Vue.component('side-bar', Sidebar)
  }
}

export default SidebarPlugin
