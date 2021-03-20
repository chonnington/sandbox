<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <!-- CSRF Token -->
      <meta name="csrf-token" content="{{ csrf_token() }}">
      <meta http-equiv="x-ua-compatible" content="ie=edge">
      <title>@yield('title', 'Your Application Name')</title>
      <!-- Font Awesome Icons -->
      <link rel="stylesheet" href="{{ url('plugins/fontawesome-free/css/all.min.css') }}">
      <link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
      <link rel="stylesheet" href="{{ url('plugins/datatables-bs4/css/dataTables.bootstrap4.min.css') }}">
      <link rel="stylesheet" href="{{ url('plugins/datatables-responsive/css/responsive.bootstrap4.min.css') }}">

      <link rel="stylesheet" href="{{ url('/css/app.css') }}">
      <link rel="stylesheet" href="{{ url('/css/custom.css') }}">

      @stack('styles')
   </head>
   <body class="hold-transition sidebar-mini">
      <div class="wrapper">
        @include('layouts.components.header')

        @include('layouts.components.sidebar')
        <!-- Content Wrapper. Contains page content -->
        <div class="content-wrapper">
            @yield('content')
        </div>
        <!-- /.content-wrapper -->
        @include('layouts.components.footer')
      </div>
      
      <script src="{{ url('/js/app.js') }}"></script>
      <script src="{{ url('plugins/jquery/jquery.min.js') }}"></script>
      <script src="{{ url('plugins/bootstrap/js/bootstrap.bundle.min.js') }}"></script>
      <script src="{{ url('plugins/datatables/jquery.dataTables.min.js') }}"></script>
      <script src="{{ url('plugins/datatables-bs4/js/dataTables.bootstrap4.min.js') }}"></script>
      <script src="{{ url('plugins/datatables-responsive/js/dataTables.responsive.min.js') }}"></script>
      <script src="{{ url('plugins/datatables-responsive/js/responsive.bootstrap4.min.js') }}"></script>
      <script src="{{ url('plugins/bs-custom-file-input/bs-custom-file-input.min.js') }}"></script>
      <script src="{{ url('plugins/inputmask/min/jquery.inputmask.bundle.min.js') }}"></script>
      <script>
         $(function () {
            $("#example1").DataTable({
               "responsive": true,
               "autoWidth": false,
            });
            
            //Money Euro
            $('[data-mask]').inputmask()
         });
      </script>
      <script>
         $(document).ready(function () {
         bsCustomFileInput.init();
         });
      </script>
      @stack('scripts')
   </body>
</html>