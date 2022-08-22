</div>
       </div>
            </body>
         </html>
         
         
         <style>
             /* The side navigation menu */
         .sidebar {
           height: 100vh;
           margin: 0;
           padding: 0;
           width: 200px;
           /* background-image: url('https://source.unsplash.com/BtbjCFUvBXs/1920x1080'); */
           background-color: #fc030b;
           position: fixed;
           height: 100%;
           overflow: auto;
         }
         
         /* Sidebar links */
         .sidebar a {
           display: block;
           color: black;
           padding: 16px;
           text-decoration: none;
         }
         
         /* Active/current link */
         .sidebar a.active {
           background-color: #04AA6D;
           color: white;
         }
         
         /* Links on mouse-over */
         .sidebar a:hover:not(.active) {
           background-color: #555;
           color: white;
         }
         
         /* Page content. The value of the margin-left property should match the value of the sidebar's width property */
         div.content {
           margin-left: 200px;
           padding: 1px 16px;
           height: 1000px;
         }
         
         /* On screens that are less than 700px wide, make the sidebar into a topbar */
         @media screen and (max-width: 700px) {
           .sidebar {
             width: 100%;
             height: auto;
             position: relative;
           }
           .sidebar a {float: left;}
           div.content {margin-left: 0;}
         }
         
         /* On screens that are less than 400px, display the bar vertically, instead of horizontally */
         @media screen and (max-width: 400px) {
           .sidebar a {
             text-align: center;
             float: none;
           }
         }
         
             /* //end */
             .masthead {
           height: 80vh;
           min-height: 300px;
           margin: 0;
           padding: 0;
           background-image: url('https://source.unsplash.com/BtbjCFUvBXs/1920x1080');
           background-size: cover;
           background-position: center;
           background-repeat: no-repeat;
         }
         a:link {
            color: black;
            text: green;
          }

         .small-box{
           height: 20vh;
           min-height: 30px;
           /* unvisited link */

           border-radius: 20px;
           background-image: url('https://media.istockphoto.com/photos/ready-for-school-concept-background-with-books-alarm-clock-and-picture-id1328368631?b=1&k=20&m=1328368631&s=170667a&w=0&h=LFcrSbsOxPcbspZJf69_xqT9iPVqzGouQ_TiohvPyoQ=');
           background-size: cover;
           background-position: center;
           background-repeat: no-repeat;
         }
         </style>