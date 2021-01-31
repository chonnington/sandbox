<!-- Main Sidebar Container -->
<aside class="main-sidebar sidebar-dark-primary elevation-4">
   <!-- Brand Logo -->
   <a href="{{url('/home')}}" class="brand-link">
   <img src="{{ url('/img/footerLogo.png') }}" alt="Vyrazu Enterprise" class="brand-image"
      style="opacity: 1">
   <span class="brand-text font-weight-light">Car-Czars</span>
   </a>
   <!-- Sidebar -->
   <div class="sidebar">
      <!-- Sidebar user panel (optional) -->
      <div class="user-panel mt-3 pb-3 mb-3 d-flex">
         <div class="image">
            <img src="{{ url('img/user2-160x160.jpg') }}" class="img-circle elevation-2" alt="User Image">
         </div>
         <div class="info">
            <a href="{{url('/userinfo')}}" class="d-block">Parmy Singh</a>
         </div>
      </div>
      <!-- Sidebar Menu -->
      <nav class="mt-2">
         <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
            <li class="nav-item">
               <a href="{{url('/test')}}" class="nav-link">
                  <i class="nav-icon fas fa-building"></i>
                  <p>
                     Users
                  </p>
               </a>
            </li>
            <!-- <li class="nav-item has-treeview">
               <a href="#" class="nav-link">
                  <i class="nav-icon fas fa-user-cog"></i>
                  <p>
                     Settings
                     <i class="right fas fa-angle-left"></i>
                  </p>
               </a>
               <ul class="nav nav-treeview">
                  <li class="nav-item">
                     <a href="#" class="nav-link">
                        <i class="far fa-circle nav-icon"></i>
                        <p>Password</p>
                     </a>
                  </li>
               </ul>
            </li> -->
         </ul>
      </nav>
      <!-- /.sidebar-menu -->
   </div>
   <!-- /.sidebar -->
</aside>