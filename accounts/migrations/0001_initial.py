<!DOCTYPE html>

<html>
  <head>
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8"/>
    
        <meta http-equiv="keywords" content="Recipes, OpenEats2, OpenEats, Django, Grocery List, Grocery Lists, Share Recipes, rated recipes"/>
    
    <meta name="description" content="Amazing Recipes and beautiful food photography. Created as well as rated by you and fellow foodies."/>
    <title>OpenEats</title>
    
        <link href="/feed/recent/" rel="alternate" type="application/rss+xml"
              title="OpenEatsTop Recipe Feed"/>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>
    <link href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.4/themes/redmond/jquery-ui.css" rel="stylesheet"/>
    
    <link rel="stylesheet" href="/static-files/bootstrap/css/bootstrap.css"/>
    <link rel="stylesheet" href="/static-files/bootstrap/css/bootstrap-flatly-theme.css"/>
    <link rel="stylesheet" href="/static-files/css/oe.css" />

     <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>

  <body>
   <nav class="navbar navbar-default navbar-fixed-top">
     <div class="container-fluid">
       <div class="navbar-header">
         <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
         </button>
         <a class="navbar-brand" href="#">OpenEats</a>
       </div>
         <div class="navbar-collapse collapse">
           
           
<ul class="nav navbar-nav">
  <li><a href="/recipe/"  title="home">home</a></li>
  <li><a href="/accounts/signIn/"  title="sign in">sign in</a></li>
  <li><a href="/about/"  title="about">about</a></li>
  <li><a href="/news/list/"  title="news">news</a></li>
  <li><a href="http://dev.openeats.org/"  title="blog">blog</a></li>
</ul>

           
           </div>
         </div><!--/.navbar-collapse -->
      </nav> <!--./navbar -->

   

   <div class="container-fluid">
     <div class="row">
       <div class="col-sm-2">
         <div class="well sidebar-nav">
           
           
           

<div id="search">
    <form method="get" class="well form-search" action="/search/" >
        <div class="row">
            <div class="col-lg-12">
                <div class="input-group">
                    <input type="text" class="form-control search-query" id="id_q" name="q">
                    <span class="input-group-btn">
                        <button class="btn btn-dark" type="submit"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></button>
                    </span>
                </div>
            </div>
        </div>
     </form>
</div>


<h4 class="page-header navheader">browse</h4>
<ul class="list-group">
    <li class="list-group-item"> <a href="/recipe/top/"> top recipes</a></li>
    <li class="list-group-item"><a href="/recipe/recent/"> recent recipes</a></li>
    
        <li class="list-group-item"><a href="/groups/course/appetizer/">appetizer</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/bread/">bread</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/breakfast/">breakfast</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/desert/">Desert</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/dessert/">dessert</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/dinner/">dinner</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/drink/">Drink</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/entree/">Entree</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/lunch/">lunch</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/meat/">meat</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/salad/">Salad</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/sauce/">sauce</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/side/">side</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/snack/">snack</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/soup/">soup</a>  </li>
    
        <li class="list-group-item"><a href="/groups/course/wine/">wine</a>  </li>
    
    
        <li class="list-group-item"> <a href="/groups/cuisine/american/">american</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/asian/">Asian</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/british/">british</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/cajun/">cajun</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/caribbean/">caribbean</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/chinese/">chinese</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/cuban/">cuban</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/french/">french</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/german/">german</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/indian/">indian</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/italian/">italian</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/japanese/">japanese</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/mediterranean/">mediterranean</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/mexican/">mexican</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/other/">Other</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/paleo/">Paleo</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/salad/">Salad</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/seafood/">Seafood</a> </li>
    
        <li class="list-group-item"> <a href="/groups/cuisine/thai/">thai</a> </li>
    
</ul>

           
         </div><!--/.well -->
       </div><!--/span-->

       <div class="col-md-9">
         
   

 <div class="jumbotron">
   <h1>OpenEats 2</h1>
    <p><p>OpenEats2 is an open source recipe management site. &nbsp;You can share recipes with friends, rate recipes, create grocery lists, store your favorite recipes to find easily, and more. &nbsp;<a href="/accounts/signIn/">Sign up</a> now for your own account to get started. &nbsp;If you want to run your own personal OpenEats site visit our <a href="https://github.com/qgriffith/OpenEats" target="_blank">code site</a>, and our development <a href="http://dev.openeats.org" target="_blank">blog</a> and <a href="http://dev.openeats.org/forum/" target="_blank">forums</a>.</p></p>
    <div id="news-photo-wrap">
      
    </div>
    <p><a class="btn btn-primary btn-lg" href="/news/entry/test-news-entry/">read more &raquo;</a></p>
</div>


    <div class="row">
     
      <div class="col-sm-9 col-md-3">
            <div class="thumbnail">
              <a href="/recipe/peach-cobbler-easy/"> <img width="230" alt="Peach Cobbler easy" src="/site-media/CACHE/images/upload/recipe_photos/PeachCobbler/b279204a181dd7ff40b4c3a4976737b7.png" class="img-thumbnail" height="230" /></a>
                <div class="caption">
                    <h4>Peach Cobbler easy</h4>
                    <p>chef: <a href="/profiles/bschumac/">bschumac</a></p>
                    <p>Delicious peach cobbler, so easy to make, so wonderful to eat!</p>
                </div>
            </div>
      </div>
     
      <div class="col-sm-9 col-md-3">
            <div class="thumbnail">
              <a href="/recipe/garlic-lime-chicken/"> <img width="230" alt="Garlic Lime Chicken" src="/site-media/CACHE/images/upload/recipe_photos/garliclime/63be686fb9047e7dab985e6aff154e09.png" class="img-thumbnail" height="230" /></a>
                <div class="caption">
                    <h4>Garlic Lime Chicken</h4>
                    <p>chef: <a href="/profiles/knuttall05/">knuttall05</a></p>
                    <p>Best if marinated for 8+ hours.</p>
                </div>
            </div>
      </div>
     
      <div class="col-sm-9 col-md-3">
            <div class="thumbnail">
              <a href="/recipe/sweet-and-sour-pork/"> <img width="230" alt="Sweet and Sour Pork" src="/site-media/CACHE/images/upload/recipe_photos/sweetnsour/337501d5dd36a3867d9dc75bf5a45313.png" class="img-thumbnail" height="230" /></a>
                <div class="caption">
                    <h4>Sweet and Sour Pork</h4>
                    <p>chef: <a href="/profiles/knuttall05/">knuttall05</a></p>
                    <p>Serve with rice</p>
                </div>
            </div>
      </div>
     
    </div>
    <div class="row">
     
      <div class="col-sm-9 col-md-3">
            <div class="thumbnail">
              <a href="/recipe/braised-pork-chops/"> <img width="230" alt="Braised Pork Chops" src="/site-media/CACHE/images/upload/recipe_photos/porkchops/3217a63d84971c362448ed1cfef427c9.png" class="img-thumbnail" height="230" /></a>
                <div class="caption">
                    <h4>Braised Pork Chops</h4>
                    <p>chef: <a href="/profiles/knuttall05/">knuttall05</a></p>
                    <p>An easy herb rub gives sensational taste to these boneless pork chops that can be cooked on the stovetop in minutes.</p>
                </div>
            </div>
      </div>
     
      <div class="col-sm-9 col-md-3">
            <div class="thumbnail">
              <a href="/recipe/blueberry-delight/"> <img width="230" alt="Blueberry Delight" src="/site-media/CACHE/images/upload/recipe_photos/blueberrydelight/639f96f753d423403e98799ad66c5e0d.png" class="img-thumbnail" height="230" /></a>
                <div class="caption">
                    <h4>Blueberry Delight</h4>
                    <p>chef: <a href="/profiles/knuttall05/">knuttall05</a></p>
                    <p>Preheat oven to 350 F</p>
                </div>
            </div>
      </div>
     
      <div class="col-sm-9 col-md-3">
            <div class="thumbnail">
              <a href="/recipe/carrot-cakecupcakes-w-cream-cheese-frosting/"> <img width="230" alt="Carrot Cake/Cupcakes w/ Cream Cheese Frosting" src="/site-media/CACHE/images/upload/recipe_photos/carrotcake/31a861593663e872cdd130f6840ab6fa.png" class="img-thumbnail" height="230" /></a>
                <div class="caption">
                    <h4>Carrot Cake/Cupcakes w/ Cream Cheese Frosting</h4>
                    <p>chef: <a href="/profiles/knuttall05/">knuttall05</a></p>
                    <p>Preheat oven to 350 F Frosting: Beat cream cheese, butter, and vanilla until creamy. Add powdered sugar and mix until smooth. Spread over cooled cake/cupcakes. 8 oz Cream Cheese, softened 1/4 lb Butter, softened 2 tsp Vanilla 1 lb Powdered Sugar &amp;nbsp; For best taste refridgerate first</p>
                </div>
            </div>
      </div>
     
    </div>

    <div id="tag-cloud" class="accordion">
      <div class="accordion-heading">
          <button class=" btn btn-primary btn-block accordion-toggle" data-toggle="collapse" data-parent="#accordion" href="#tagcloud">
              <span class="glyphicon glyphicon-tags" aria-hidden="true"></span> recipe tags
          </button>
      </div>
      <div id="tagcloud" class="accordion-body collapse">
        
        <ul class="well">
          
            <li><a href="/tags/recipe/200-300-kcal/" class="tag1">200-300 Kcal</a></li>
          
            <li><a href="/tags/recipe/344/" class="tag1">344</a></li>
          
            <li><a href="/tags/recipe/400-500-kcal/" class="tag1">400-500 kcal</a></li>
          
            <li><a href="/tags/recipe/american/" class="tag2">american</a></li>
          
            <li><a href="/tags/recipe/apple-juice/" class="tag1">apple juice</a></li>
          
            <li><a href="/tags/recipe/apples/" class="tag1">apples</a></li>
          
            <li><a href="/tags/recipe/apples-mustard/" class="tag1">apples. mustard</a></li>
          
            <li><a href="/tags/recipe/apricots/" class="tag1">apricots</a></li>
          
            <li><a href="/tags/recipe/asian/" class="tag2">asian</a></li>
          
            <li><a href="/tags/recipe/asparagus/" class="tag1">asparagus</a></li>
          
            <li><a href="/tags/recipe/aubergines/" class="tag1">aubergines</a></li>
          
            <li><a href="/tags/recipe/bagels/" class="tag1">bagels</a></li>
          
            <li><a href="/tags/recipe/balls/" class="tag1">balls</a></li>
          
            <li><a href="/tags/recipe/balsamic/" class="tag1">balsamic</a></li>
          
            <li><a href="/tags/recipe/banan/" class="tag1">banan</a></li>
          
            <li><a href="/tags/recipe/bars/" class="tag1">bars</a></li>
          
            <li><a href="/tags/recipe/basil/" class="tag1">basil</a></li>
          
            <li><a href="/tags/recipe/bbq/" class="tag2">bbq</a></li>
          
            <li><a href="/tags/recipe/bean/" class="tag1">Bean</a></li>
          
            <li><a href="/tags/recipe/beans/" class="tag1">beans</a></li>
          
            <li><a href="/tags/recipe/beef/" class="tag2">beef</a></li>
          
            <li><a href="/tags/recipe/beer/" class="tag1">beer</a></li>
          
            <li><a href="/tags/recipe/berries/" class="tag1">berries</a></li>
          
            <li><a href="/tags/recipe/birthday/" class="tag1">birthday</a></li>
          
            <li><a href="/tags/recipe/blue-cheese/" class="tag1">blue cheese</a></li>
          
            <li><a href="/tags/recipe/bourbon/" class="tag1">bourbon</a></li>
          
            <li><a href="/tags/recipe/brats/" class="tag1">brats</a></li>
          
            <li><a href="/tags/recipe/brazilian/" class="tag1">brazilian</a></li>
          
            <li><a href="/tags/recipe/bread/" class="tag2">bread</a></li>
          
            <li><a href="/tags/recipe/breakfast/" class="tag2">breakfast</a></li>
          
            <li><a href="/tags/recipe/breast/" class="tag1">breast</a></li>
          
            <li><a href="/tags/recipe/broccoli/" class="tag1">broccoli</a></li>
          
            <li><a href="/tags/recipe/bruschetta/" class="tag1">bruschetta</a></li>
          
            <li><a href="/tags/recipe/bulguar/" class="tag1">bulguar</a></li>
          
            <li><a href="/tags/recipe/burger/" class="tag1">burger</a></li>
          
            <li><a href="/tags/recipe/burrito/" class="tag1">burrito</a></li>
          
            <li><a href="/tags/recipe/burrito_1/" class="tag1">Burrito</a></li>
          
            <li><a href="/tags/recipe/butter/" class="tag1">butter</a></li>
          
            <li><a href="/tags/recipe/butterfly/" class="tag1">butterfly</a></li>
          
            <li><a href="/tags/recipe/cajun/" class="tag1">cajun</a></li>
          
            <li><a href="/tags/recipe/candy/" class="tag1">candy</a></li>
          
            <li><a href="/tags/recipe/carbonara/" class="tag1">carbonara</a></li>
          
            <li><a href="/tags/recipe/carribean/" class="tag1">carribean</a></li>
          
            <li><a href="/tags/recipe/carrot-cake/" class="tag1">carrot cake</a></li>
          
            <li><a href="/tags/recipe/cauliflower/" class="tag1">Cauliflower</a></li>
          
            <li><a href="/tags/recipe/cereal/" class="tag1">cereal</a></li>
          
            <li><a href="/tags/recipe/cheese/" class="tag1">Cheese</a></li>
          
            <li><a href="/tags/recipe/cheesecake/" class="tag1">cheesecake</a></li>
          
            <li><a href="/tags/recipe/chewy/" class="tag1">chewy</a></li>
          
            <li><a href="/tags/recipe/chia/" class="tag1">Chia</a></li>
          
            <li><a href="/tags/recipe/chicken_1/" class="tag1">Chicken</a></li>
          
            <li><a href="/tags/recipe/chicken/" class="tag6">chicken</a></li>
          
            <li><a href="/tags/recipe/chicken-legs/" class="tag1">chicken legs</a></li>
          
            <li><a href="/tags/recipe/chili/" class="tag1">chili</a></li>
          
            <li><a href="/tags/recipe/chinese/" class="tag1">chinese</a></li>
          
            <li><a href="/tags/recipe/chocolate/" class="tag1">chocolate</a></li>
          
            <li><a href="/tags/recipe/chocolate-chip-cookies/" class="tag1">chocolate chip cookies</a></li>
          
            <li><a href="/tags/recipe/chocolate-chips/" class="tag1">chocolate chips</a></li>
          
            <li><a href="/tags/recipe/christmas/" class="tag2">christmas</a></li>
          
            <li><a href="/tags/recipe/christmas_1/" class="tag1">Christmas</a></li>
          
            <li><a href="/tags/recipe/cobbler/" class="tag1">cobbler</a></li>
          
            <li><a href="/tags/recipe/cocktail/" class="tag1">cocktail</a></li>
          
            <li><a href="/tags/recipe/coconut/" class="tag1">coconut</a></li>
          
            <li><a href="/tags/recipe/cookies_1/" class="tag1">Cookies</a></li>
          
            <li><a href="/tags/recipe/cookies/" class="tag1">cookies</a></li>
          
            <li><a href="/tags/recipe/cornish/" class="tag1">cornish</a></li>
          
            <li><a href="/tags/recipe/courgette/" class="tag1">courgette</a></li>
          
            <li><a href="/tags/recipe/cranberry-sauce/" class="tag1">cranberry sauce</a></li>
          
            <li><a href="/tags/recipe/cream-cheese/" class="tag1">cream cheese</a></li>
          
            <li><a href="/tags/recipe/crock-pot/" class="tag2">crock pot</a></li>
          
            <li><a href="/tags/recipe/crockpot/" class="tag2">crockpot</a></li>
          
            <li><a href="/tags/recipe/cuban/" class="tag1">cuban</a></li>
          
            <li><a href="/tags/recipe/cumin/" class="tag1">cumin</a></li>
          
            <li><a href="/tags/recipe/delicious/" class="tag1">delicious</a></li>
          
            <li><a href="/tags/recipe/dessert/" class="tag2">dessert</a></li>
          
            <li><a href="/tags/recipe/deviled/" class="tag1">deviled</a></li>
          
            <li><a href="/tags/recipe/diet/" class="tag1">diet</a></li>
          
            <li><a href="/tags/recipe/dinner/" class="tag2">dinner</a></li>
          
            <li><a href="/tags/recipe/dip/" class="tag1">dip</a></li>
          
            <li><a href="/tags/recipe/easter/" class="tag1">easter</a></li>
          
            <li><a href="/tags/recipe/easy_1/" class="tag1">Easy</a></li>
          
            <li><a href="/tags/recipe/easy/" class="tag2">easy</a></li>
          
            <li><a href="/tags/recipe/eber/" class="tag1">Éber</a></li>
          
            <li><a href="/tags/recipe/eggs/" class="tag1">eggs</a></li>
          
            <li><a href="/tags/recipe/enchiladas/" class="tag1">enchiladas</a></li>
          
            <li><a href="/tags/recipe/enery/" class="tag1">enery</a></li>
          
            <li><a href="/tags/recipe/entree/" class="tag1">entree</a></li>
          
            <li><a href="/tags/recipe/fajitas/" class="tag1">fajitas</a></li>
          
            <li><a href="/tags/recipe/fall/" class="tag2">fall</a></li>
          
            <li><a href="/tags/recipe/family-recipe/" class="tag1">family recipe</a></li>
          
            <li><a href="/tags/recipe/farfalle/" class="tag1">farfalle</a></li>
          
            <li><a href="/tags/recipe/feta/" class="tag1">feta</a></li>
          
            <li><a href="/tags/recipe/fish/" class="tag1">fish</a></li>
          
            <li><a href="/tags/recipe/flourless/" class="tag1">flourless</a></li>
          
            <li><a href="/tags/recipe/fondue/" class="tag1">fondue</a></li>
          
            <li><a href="/tags/recipe/free/" class="tag1">Free</a></li>
          
            <li><a href="/tags/recipe/frosting/" class="tag1">frosting</a></li>
          
            <li><a href="/tags/recipe/fruit/" class="tag1">fruit</a></li>
          
            <li><a href="/tags/recipe/garlic/" class="tag2">garlic</a></li>
          
            <li><a href="/tags/recipe/gazpacho/" class="tag1">gazpacho</a></li>
          
            <li><a href="/tags/recipe/german/" class="tag1">german</a></li>
          
            <li><a href="/tags/recipe/gluten/" class="tag1">Gluten</a></li>
          
            <li><a href="/tags/recipe/gluten-free/" class="tag2">Gluten Free</a></li>
          
            <li><a href="/tags/recipe/gluten-free_1/" class="tag2">gluten free</a></li>
          
            <li><a href="/tags/recipe/gluten-free_2/" class="tag1">GLuten Free</a></li>
          
            <li><a href="/tags/recipe/goat-cheese/" class="tag2">goat cheese</a></li>
          
            <li><a href="/tags/recipe/graam/" class="tag1">graam</a></li>
          
            <li><a href="/tags/recipe/grain-free/" class="tag1">grain free</a></li>
          
            <li><a href="/tags/recipe/granola/" class="tag1">granola</a></li>
          
            <li><a href="/tags/recipe/greek/" class="tag1">Greek</a></li>
          
            <li><a href="/tags/recipe/grill/" class="tag3">grill</a></li>
          
            <li><a href="/tags/recipe/grilled/" class="tag1">grilled</a></li>
          
            <li><a href="/tags/recipe/groente/" class="tag1">groente</a></li>
          
            <li><a href="/tags/recipe/ground-beef/" class="tag1">ground beef</a></li>
          
            <li><a href="/tags/recipe/grd/" class="tag1">Grød</a></li>
          
            <li><a href="/tags/recipe/healthy/" class="tag3">healthy</a></li>
          
            <li><a href="/tags/recipe/holiday/" class="tag2">holiday</a></li>
          
            <li><a href="/tags/recipe/honey/" class="tag1">honey</a></li>
          
            <li><a href="/tags/recipe/hunters-chicken/" class="tag1">hunters chicken</a></li>
          
            <li><a href="/tags/recipe/indian/" class="tag1">indian</a></li>
          
            <li><a href="/tags/recipe/italian/" class="tag2">italian</a></li>
          
            <li><a href="/tags/recipe/itilian/" class="tag1">itilian</a></li>
          
            <li><a href="/tags/recipe/lamb/" class="tag1">lamb</a></li>
          
            <li><a href="/tags/recipe/lard/" class="tag1">lard</a></li>
          
            <li><a href="/tags/recipe/lasagne/" class="tag1">lasagne</a></li>
          
            <li><a href="/tags/recipe/lean/" class="tag1">lean</a></li>
          
            <li><a href="/tags/recipe/lemon/" class="tag1">lemon</a></li>
          
            <li><a href="/tags/recipe/london-broil/" class="tag1">london broil</a></li>
          
            <li><a href="/tags/recipe/low-fat/" class="tag2">low fat</a></li>
          
            <li><a href="/tags/recipe/low-fat_1/" class="tag1">low-fat</a></li>
          
            <li><a href="/tags/recipe/lunch/" class="tag1">lunch</a></li>
          
            <li><a href="/tags/recipe/mango/" class="tag2">mango</a></li>
          
            <li><a href="/tags/recipe/marindade/" class="tag1">marindade</a></li>
          
            <li><a href="/tags/recipe/meat/" class="tag2">meat</a></li>
          
            <li><a href="/tags/recipe/meat_1/" class="tag1">Meat</a></li>
          
            <li><a href="/tags/recipe/mexican/" class="tag2">mexican</a></li>
          
            <li><a href="/tags/recipe/microwave/" class="tag1">microwave</a></li>
          
            <li><a href="/tags/recipe/mike/" class="tag1">mike</a></li>
          
            <li><a href="/tags/recipe/modified/" class="tag1">Modified</a></li>
          
            <li><a href="/tags/recipe/mojo/" class="tag1">mojo</a></li>
          
            <li><a href="/tags/recipe/naan/" class="tag1">naan</a></li>
          
            <li><a href="/tags/recipe/nanchos/" class="tag1">nanchos</a></li>
          
            <li><a href="/tags/recipe/needs-prep/" class="tag1">needs prep</a></li>
          
            <li><a href="/tags/recipe/new-york/" class="tag1">new york</a></li>
          
            <li><a href="/tags/recipe/noodles/" class="tag1">noodles</a></li>
          
            <li><a href="/tags/recipe/oatmeal/" class="tag1">oatmeal</a></li>
          
            <li><a href="/tags/recipe/oats/" class="tag1">oats</a></li>
          
            <li><a href="/tags/recipe/open-access/" class="tag1">Open Access</a></li>
          
            <li><a href="/tags/recipe/p90x/" class="tag4">p90x</a></li>
          
            <li><a href="/tags/recipe/paleo_1/" class="tag2">paleo</a></li>
          
            <li><a href="/tags/recipe/paleo/" class="tag2">Paleo</a></li>
          
            <li><a href="/tags/recipe/pancakes/" class="tag1">pancakes</a></li>
          
            <li><a href="/tags/recipe/party/" class="tag1">party</a></li>
          
            <li><a href="/tags/recipe/pasta/" class="tag2">pasta</a></li>
          
            <li><a href="/tags/recipe/pasta_1/" class="tag1">Pasta</a></li>
          
            <li><a href="/tags/recipe/pasta-substitute/" class="tag1">Pasta Substitute</a></li>
          
            <li><a href="/tags/recipe/peach/" class="tag1">peach</a></li>
          
            <li><a href="/tags/recipe/peanut-butter/" class="tag1">peanut butter</a></li>
          
            <li><a href="/tags/recipe/peanut-butter-chips/" class="tag1">peanut butter chips</a></li>
          
            <li><a href="/tags/recipe/pie/" class="tag1">pie</a></li>
          
            <li><a href="/tags/recipe/pit-barrel/" class="tag1">pit barrel</a></li>
          
            <li><a href="/tags/recipe/pizza/" class="tag1">pizza</a></li>
          
            <li><a href="/tags/recipe/pizza-crust/" class="tag1">Pizza Crust</a></li>
          
            <li><a href="/tags/recipe/pork/" class="tag3">pork</a></li>
          
            <li><a href="/tags/recipe/pork-chop/" class="tag1">pork chop</a></li>
          
            <li><a href="/tags/recipe/pork-chops/" class="tag1">pork chops</a></li>
          
            <li><a href="/tags/recipe/portabella/" class="tag1">portabella</a></li>
          
            <li><a href="/tags/recipe/potatoes/" class="tag1">potatoes</a></li>
          
            <li><a href="/tags/recipe/potatos/" class="tag1">potatos</a></li>
          
            <li><a href="/tags/recipe/prawn/" class="tag1">prawn</a></li>
          
            <li><a href="/tags/recipe/prime-rib/" class="tag1">prime rib</a></li>
          
            <li><a href="/tags/recipe/protein/" class="tag1">protein</a></li>
          
            <li><a href="/tags/recipe/protien/" class="tag1">protien</a></li>
          
            <li><a href="/tags/recipe/pub/" class="tag1">pub</a></li>
          
            <li><a href="/tags/recipe/puff-pastry/" class="tag1">puff pastry</a></li>
          
            <li><a href="/tags/recipe/pumpkin/" class="tag1">pumpkin</a></li>
          
            <li><a href="/tags/recipe/quick/" class="tag1">quick</a></li>
          
            <li><a href="/tags/recipe/quinoa/" class="tag1">Quinoa</a></li>
          
            <li><a href="/tags/recipe/rib-roast/" class="tag1">rib roast</a></li>
          
            <li><a href="/tags/recipe/riceable/" class="tag1">riceable</a></li>
          
            <li><a href="/tags/recipe/risengrd/" class="tag1">Risengrød</a></li>
          
            <li><a href="/tags/recipe/risotto/" class="tag1">Risotto</a></li>
          
            <li><a href="/tags/recipe/rolls/" class="tag1">rolls</a></li>
          
            <li><a href="/tags/recipe/rosemary/" class="tag1">rosemary</a></li>
          
            <li><a href="/tags/recipe/running/" class="tag1">running</a></li>
          
            <li><a href="/tags/recipe/sage/" class="tag1">sage</a></li>
          
            <li><a href="/tags/recipe/salad/" class="tag2">salad</a></li>
          
            <li><a href="/tags/recipe/salmon/" class="tag1">salmon</a></li>
          
            <li><a href="/tags/recipe/salsa/" class="tag1">salsa</a></li>
          
            <li><a href="/tags/recipe/sandwich/" class="tag2">sandwich</a></li>
          
            <li><a href="/tags/recipe/sauce/" class="tag1">sauce</a></li>
          
            <li><a href="/tags/recipe/sausage/" class="tag1">sausage</a></li>
          
            <li><a href="/tags/recipe/sb2/" class="tag1">SB2</a></li>
          
            <li><a href="/tags/recipe/seafood/" class="tag1">seafood</a></li>
          
            <li><a href="/tags/recipe/shake/" class="tag1">shake</a></li>
          
            <li><a href="/tags/recipe/share/" class="tag1">Share</a></li>
          
            <li><a href="/tags/recipe/shrimp/" class="tag2">shrimp</a></li>
          
            <li><a href="/tags/recipe/side/" class="tag1">side</a></li>
          
            <li><a href="/tags/recipe/side-dish/" class="tag2">side dish</a></li>
          
            <li><a href="/tags/recipe/slowcarb/" class="tag1">slowcarb</a></li>
          
            <li><a href="/tags/recipe/soup/" class="tag3">soup</a></li>
          
            <li><a href="/tags/recipe/southern/" class="tag1">southern</a></li>
          
            <li><a href="/tags/recipe/spicy/" class="tag1">spicy</a></li>
          
            <li><a href="/tags/recipe/steak/" class="tag2">steak</a></li>
          
            <li><a href="/tags/recipe/stir-fry/" class="tag1">stir fry</a></li>
          
            <li><a href="/tags/recipe/strawberries/" class="tag1">strawberries</a></li>
          
            <li><a href="/tags/recipe/stuffing/" class="tag1">stuffing</a></li>
          
            <li><a href="/tags/recipe/summer/" class="tag1">summer</a></li>
          
            <li><a href="/tags/recipe/sweet/" class="tag1">sweet</a></li>
          
            <li><a href="/tags/recipe/taco-shell/" class="tag1">Taco Shell</a></li>
          
            <li><a href="/tags/recipe/test/" class="tag1">test</a></li>
          
            <li><a href="/tags/recipe/thai/" class="tag1">thai</a></li>
          
            <li><a href="/tags/recipe/thanksgiving/" class="tag2">thanksgiving</a></li>
          
            <li><a href="/tags/recipe/thermomix/" class="tag2">Thermomix</a></li>
          
            <li><a href="/tags/recipe/tofu/" class="tag1">tofu</a></li>
          
            <li><a href="/tags/recipe/tostada/" class="tag1">tostada</a></li>
          
            <li><a href="/tags/recipe/turkey/" class="tag1">turkey</a></li>
          
            <li><a href="/tags/recipe/turkey-breast/" class="tag1">turkey breast</a></li>
          
            <li><a href="/tags/recipe/vegan/" class="tag1">vegan</a></li>
          
            <li><a href="/tags/recipe/vegetables/" class="tag1">vegetables</a></li>
          
            <li><a href="/tags/recipe/vegetarian/" class="tag3">vegetarian</a></li>
          
            <li><a href="/tags/recipe/vegetarish/" class="tag1">Vegetarish</a></li>
          
            <li><a href="/tags/recipe/wellington/" class="tag1">wellington</a></li>
          
            <li><a href="/tags/recipe/wheat-free/" class="tag1">wheat free</a></li>
          
            <li><a href="/tags/recipe/wine/" class="tag1">wine</a></li>
          
            <li><a href="/tags/recipe/winter/" class="tag2">winter</a></li>
          
            <li><a href="/tags/recipe/yoghurt/" class="tag1">yoghurt</a></li>
          
            <li><a href="/tags/recipe/yum/" class="tag1">Yum</a></li>
          
            <li><a href="/tags/recipe/zucchini/" class="tag1">Zucchini</a></li>
          
        </ul>
      </div>
    </div>


       </div>
     </div><!--/row-->

     <hr>

     <footer>
        &copy;OpenEats 2015
    </footer>
   </div><!--/.fluid-container-->

    <!-- javascript
   ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/static-files/bootstrap/js/bootstrap.js"></script>
    <script type="text/javascript" src="/static-files/js/oe.js"></script>


  </body>
</html>
