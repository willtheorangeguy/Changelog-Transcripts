[0.00 --> 8.04]  what is up everyone adam stakowiak here editor-in-chief of changelog we teamed up with some
[8.04 --> 13.12]  friends of ours over at heroku to promote their podcast called codish you can check it out at
[13.12 --> 19.20]  heroku.com slash podcasts slash codish and today we're dropping a full-length episode right here
[19.20 --> 24.94]  in the js party feed featuring o and o of heroku joined by tamai gopal talking about the pros and
[24.94 --> 39.22]  cons of using graphql in your applications here we go hello and welcome to codish an exploration
[39.22 --> 45.28]  of the lives of modern developers join us as we dive into topics like languages and frameworks
[45.28 --> 51.68]  data and event-driven architectures and individual and team productivity all tailored to developers
[51.68 --> 56.62]  and engineering leaders this episode is part of our deeply technical series
[56.62 --> 67.98]  hello welcome to the codish podcast my name is o10 i'm an engineer from heroku with me today we have
[67.98 --> 77.12]  tamai gopal a ceo from a company called hasaru today we are going to talk about graphql so what is
[77.12 --> 85.50]  graphql and what is the motivation behind it graphql is uh api specification very similar to rest
[85.50 --> 93.58]  and very similar to soap before that and it's an api specification that focuses on making data fetch
[93.58 --> 101.06]  kind of api calls easy especially for front-end applications it is a specification that is agnostic to
[101.06 --> 109.00]  language or framework um and even protocol so you can implement graphql on top of http or something else
[109.00 --> 114.94]  and you can implement a graphql server and a graphql client in any language uh in any framework
[114.94 --> 121.70]  and it is independent to that again very similar to the way rest and so forth the key motivation behind
[121.70 --> 128.96]  graphql was um to make it easier for uh front-end developers um and application developers
[128.96 --> 136.14]  to make api calls um and to fetch data from api calls there are some nuances around that and i can
[136.14 --> 140.90]  i can dive deeper but um it was primarily designed for application developers to be able to build
[140.90 --> 147.52]  quickly and to be able to integrate apis and use apis inside their applications faster yeah that's
[147.52 --> 154.56]  excellent so you mentioned about client-side application so like what kind of client-side application
[154.56 --> 161.64]  are you talking about a browser app or a crr app yeah i'm talking about i'm talking about browser
[161.64 --> 167.90]  applications or i'm talking about web applications and mobile applications in fact graphql first started
[167.90 --> 173.84]  getting used in facebook for the ios application so even for mobile applications but basically
[173.84 --> 180.04]  developers were kind of building front-end user-facing applications uh it's it was primarily designed for
[180.04 --> 185.38]  then but graphql just like any other api can technically use any client and server but you can
[185.38 --> 191.80]  see direct features in the design that make it very suitable for front-end applications got it so
[191.80 --> 198.06]  graphql would be another one that i consider if i implement my client application so maybe before
[198.06 --> 204.82]  comparing rest with graphql what would be the cost and benefit of implementing graphql so so there are
[204.82 --> 210.66]  technical costs and benefits of course to implementing graphql but one of the most important
[210.66 --> 218.32]  motivations or kind of i think the primary benefit to graphql and where graphql shines is going to be
[218.32 --> 226.22]  where you are building a web api and the consumers of your api are mostly going to be front-end applications
[226.22 --> 231.14]  right so that's that's the case where you would think about saying well maybe maybe i don't expose a
[231.14 --> 236.88]  best api but you know maybe i expose a graphql api and and the reason why this has a tremendous
[236.88 --> 241.58]  amount of benefit is because like as a front-end developer if i wear the shoes of a front-end
[241.58 --> 246.40]  developer i love building out the application i love caring about the user experience i love
[246.40 --> 253.26]  making sure that users you know love the product that i build but the part that i hate is the part
[253.26 --> 259.36]  where i need to integrate apis to actually make the application work right and and this bit is painful
[259.36 --> 264.62]  because traditionally with apis you know if you just think about integrating an api the first thing
[264.62 --> 270.90]  is that most modern applications today the same screen that you look at the same web page or the
[270.90 --> 276.14]  same mobile screen that you're looking at you you actually make a variety of api calls to kind of
[276.14 --> 280.46]  different things right maybe you're making a sas api api call to a sas service maybe you're making an
[280.46 --> 284.94]  api call to your own web server you're fetching different kinds of resources let's say for example
[284.94 --> 289.74]  you're building a profile page you know you need to you need to make an api call to fetch the user
[289.74 --> 294.40]  information like the user name and email and then maybe you need to make another api call to fetch the
[294.40 --> 299.14]  address information you want to show that you know the last five addresses of this user on their profile
[299.14 --> 304.54]  page so you make another api call for doing that and soon you realize that for kind of pages that are
[304.54 --> 309.98]  becoming complicated you realize that you as a front-end developer start making you know lots of api calls
[309.98 --> 316.08]  and this process is painful because you have api calls are asynchronous so you know you you make an
[316.08 --> 320.78]  api call you wait for the network to kind of give you data and then the user is kind of blocked till
[320.78 --> 326.04]  then and then they kind of see data coming in right and imagine if you have like five or six api calls
[326.04 --> 330.66]  you just have different parts of the screen kind of loading in different speeds or you know you have
[330.66 --> 335.58]  to take care of issues like that and these are things that you'd already figured out when you built the
[335.58 --> 341.40]  app but then when you did the api integration you know everything was it wasn't fun and um and this
[341.40 --> 345.86]  is not a new problem right this is a fairly old problem and so what people started doing was they
[345.86 --> 350.98]  said you know we'll have something like a bff like a back end for front end um and we'll aggregate this
[350.98 --> 356.38]  api so we'll give we'll provide one api where you can fetch all the other five like resources that
[356.38 --> 361.98]  you wanted and show that on your screen this was kind of becoming a pattern um meanwhile simultaneously
[361.98 --> 368.22]  on the facebook side they said you know what what if we create um and what if we like think about all
[368.22 --> 373.96]  these problems that front end developers face and we kind of solve this problem more systematically right
[373.96 --> 380.78]  so what they did was they said instead of making a bunch of api calls why don't we all have a single
[380.78 --> 386.64]  api endpoint let's give this endpoint to the front end developer team and and what that dev team can do
[386.64 --> 392.52]  is say i can make an api call and instead of you know specifying the resource that i want as a part
[392.52 --> 400.02]  of the url so instead of saying something like i want to get a slash user or slash user a slash address
[400.02 --> 405.34]  instead of saying something like that you can now say you know slash graphql and what you submit to
[405.34 --> 413.26]  this endpoint is a query so you make a post request where you submit a query and you say i want i query
[413.26 --> 421.08]  for user and within user i want id comma name and i want address and within address which is like uh you
[421.08 --> 427.92]  know like a nested node inside the user object i want um address dot id address dot street address dot
[427.92 --> 434.56]  city address dot country right and you can specify exactly the shape uh of the resource that you want
[434.56 --> 440.26]  and the graphql server then kind of figures out that okay you need to fetch like three or four different
[440.26 --> 447.00]  resources so uh let's make this uh api call and and let's let's fetch all these resources and let's
[447.00 --> 451.06]  send these resources to the front end so from the front end developers point of view now it's a great
[451.06 --> 457.02]  experience right because now i can make one api call i can specify in that api my query and i can get
[457.02 --> 463.06]  exactly the data that i want um and so this is a huge benefit to the front end developer what you're
[463.06 --> 472.10]  saying is graphql allow me to have one endpoint that can query all the domain logic that i want to
[472.10 --> 479.06]  query exactly exactly and it's very similar to imagine that as uh you know as as maybe if you're
[479.06 --> 485.80]  building a web api right uh as a developer you have something like sql or like you know a query language
[485.80 --> 492.24]  mongo or something like that you have you have you have sql and using sql you can query everything in
[492.24 --> 497.22]  the database right you can you can query anything in the database that you want and sql is great for
[497.22 --> 503.08]  doing that um but imagine if the database gave you like rest endpoints right wouldn't you be like it
[503.08 --> 506.88]  would be so irritating for the backend developer because every time you want to like you know
[506.88 --> 511.82]  fetch something interesting you want to maybe do a join you want to do some filtering it's so
[511.82 --> 516.06]  inconvenient because you kind of want to fetch you want to make a better query for fetching you know
[516.06 --> 522.16]  the entire kind of quote unquote graph or relationship structure that you want um graphql is
[522.16 --> 528.96]  very analogous to that power it gives the frontend developer that kind of power right that kind of
[528.96 --> 535.46]  flexibility in saying here are the domain resources and here's my query for fetching the precise slice
[535.46 --> 541.10]  of domain resources that i want and that power is so amazing for frontend developers because now they
[541.10 --> 546.46]  don't have to wait for backend developers to create new endpoints right they can always query for exactly
[546.46 --> 551.48]  what they want um as long as somehow the domain models are represented on the backend um it's a great
[551.48 --> 557.88]  experience for frontend developers so how would i get started creating a graphql application
[557.88 --> 566.62]  do i define some sort of schema to open up my api endpoint or how would i get started it's very
[566.62 --> 571.02]  similar to how you would get started with uh with how you would get started with building just a normal
[571.02 --> 576.94]  api and a client server web application right so you on the frontend um you know you're building your
[576.94 --> 581.76]  app you start making api calls and you use something like a rest client or you use some kind of http
[581.76 --> 586.02]  client so on the frontend you know you build your frontend but instead of using an http client
[586.02 --> 592.54]  you use a graphql client and a graphql client is basically a simple wrapper on top of an http client
[592.54 --> 597.60]  which allows you to conveniently create queries um and then you know you don't have to put in the
[597.60 --> 601.54]  exact url and the parameters you just have to submit you just write out your graphql query
[601.54 --> 607.56]  and you get the data and then you can start using that data in your application and on the backend
[607.56 --> 613.00]  um very similar to how you have um you know how you would build a rest server or like you know maybe
[613.00 --> 619.06]  just an api server uh the typical pattern is that you create something like a routes file or a urls
[619.06 --> 624.24]  file right and so you specify the different url paths and the different resources that you want to
[624.24 --> 629.64]  make available so maybe you still have a get endpoint for user you have a get endpoint for user address
[629.64 --> 635.58]  you have a post endpoint for um you know creating a user and stuff like that um and then you would
[635.58 --> 643.78]  have in in the in the in the rest api world you would have kind of mapped these urls to functions
[643.78 --> 651.14]  and these functions or controllers would have actually um executed some kind of data fetching logic or some
[651.14 --> 657.98]  security and authorization logic and then uh return that data or return that json um in in the graphql
[657.98 --> 665.86]  world it's very similar but instead of mapping urls to functions what you do is you map uh you create
[665.86 --> 673.64]  graphql uh types right so you say i have a user type and i have let's say an address type and every user
[673.64 --> 680.52]  has an address and so what you do is you say this is the user type i'm going to have an address field
[680.52 --> 686.34]  inside the user type which is a reference to the address type right so you kind of create
[686.34 --> 692.52]  these two types that are linked to each other um and then for each each of these kind of types or
[692.52 --> 699.66]  fields you attach a function so you say that if somebody requests for the user like field or the
[699.66 --> 706.42]  user type then this function can execute the logic for fetching the exact data for user right and
[706.42 --> 711.64]  similarly for address you specify a function and you say this function knows how to fetch the address
[711.64 --> 718.46]  information so now if the front-end application makes a query and says i want user id one uh name
[718.46 --> 723.76]  and address and for address i want address dot city right so what happens is your server will execute the
[723.76 --> 729.30]  function for user execute the function for address it will run these two functions and then kind of get
[729.30 --> 734.84]  the data put it into a json structure and then respond to the client so very similar to what you would
[734.84 --> 740.86]  have done like no magic it's just that instead of instead of having something that can process a url and map it
[740.86 --> 746.94]  to a function you instead process a query and map it to a function um these functions are called resolvers
[746.94 --> 754.90]  so you map fields to resolvers like you map urls to controllers uh very similar um so what what would be
[754.90 --> 761.76]  a case is that graphql would not be a good fit so a graphql api um you know from the description like i was
[761.76 --> 767.86]  i was giving you it seems it would be it's quite clear that if you have uh you know you you can model your
[767.86 --> 772.96]  uh domain objects with a schema and then every time i make a request you return some json data
[772.96 --> 779.32]  right um that itself will kind of point out those conditions where you realize that graphql is not a
[779.32 --> 784.32]  good fit for example if you have binary data right let's say for example i make a request and i say
[784.32 --> 789.72]  i want to fetch an image right or i want to fetch a video right or i need to fetch a stream
[789.72 --> 796.88]  of of some data um in those cases graphql is not ideal or even if the return if the return if the response
[796.88 --> 803.02]  is not json well that's a pretty clear fit for not being a great fit for graphql uh but even if you
[803.02 --> 807.66]  have things like streaming or you have binary data that's not a good fit for graphql as well and
[807.66 --> 813.82]  sometimes depending on the application that you have uh you know you you might not you you you might
[813.82 --> 820.78]  realize that the way that you're modeling uh the way that your api models are built uh it doesn't
[820.78 --> 825.36]  really fit with graphql or you know maybe it's very chatty maybe the client and the server are
[825.36 --> 829.88]  kind of very chatty maybe it's an internal application it's very chatty um and it's it's
[829.88 --> 835.74]  not a great fit for graphql but in most applications that we think about in the web and mobile landscape
[835.74 --> 842.08]  graphql actually ends up being a really good fit so now let's change a little bit of the topic to
[842.08 --> 851.12]  uh the adoption of graphql what is driving graphql adoption today graphql makes the front end and the
[851.12 --> 857.90]  dev the app dev team it gives them superpowers right it makes them very productive so in all of
[857.90 --> 864.44]  the cases where the end user application and the quality of the end user application and the
[864.44 --> 870.42]  agility of being able to add remove and iterate on features of the end user application is important
[870.42 --> 878.28]  graphql becomes very useful so wherever we notice that the business drivers are closely correlated to
[878.28 --> 884.28]  the quality of the end user application graphql starts kind of sneaking in and the front end team
[884.28 --> 889.30]  says you know what if you want us to be productive give us a graphql api um and that's kind of the
[889.30 --> 894.16]  primary vector um and that kind of also answers situations where you know graphql is not a primary
[894.16 --> 898.48]  vector right so that's kind of the primary reason and and what and what we notice in the world today is
[898.48 --> 904.34]  that so much of the way that we use technology and the way people are using technology has shifted
[904.34 --> 911.58]  to being able to provide a good user experience on on an application right and so many things uh for
[911.58 --> 917.00]  any business right whether it's a consumer like a startup or a large technology giant or whether it's
[917.00 --> 923.84]  a enterprise um you know even if it's like a small store um so much of the way that they deliver
[923.84 --> 929.60]  technology to their end users is shifting to the front end right and the and the power of the
[929.60 --> 934.50]  application on the front end that graphql is becoming important um and i think those two factors
[934.50 --> 941.62]  combined uh are kind of causing a massive amount of graphql buzz uh for in the front end ecosystem
[941.62 --> 948.76]  now let's change the topic a little bit to the best practices of uh using graphql what are some of the
[948.76 --> 954.48]  best practices in your opinion for using graphql i think it depends a lot on the existing situation
[954.48 --> 959.54]  that you have you know maybe uh let's say for example you have a monolithic application
[959.54 --> 964.90]  or let's say you have micro services um let's say you don't have front end applications and you have
[964.90 --> 970.32]  mostly service to service communication uh or you know and so you have kind of different scenarios right
[970.32 --> 974.08]  let's say you're building a new application or let's say you're kind of adding graphql to an existing
[974.08 --> 978.90]  application um and so in all of those scenarios the kind of different things are the best practices
[978.90 --> 986.12]  of using graphql very um but uh what what is um and and if i can kind of break down these individual
[986.12 --> 992.24]  scenarios uh one by one if you have an existing monolith and you want to use graphql there is good
[992.24 --> 997.66]  tooling today so what you would do is you would use a graphql kind of i won't say framework but you
[997.66 --> 1003.56]  will use something like a graphql module or a graphql library and this graphql library will allow you
[1003.56 --> 1009.56]  to create a graphql schema and map those graphql schemas to resolvers and these resolvers that you
[1009.56 --> 1014.40]  implement will kind of talk to the underlying controllers that you have within the monolith
[1014.40 --> 1021.24]  and in this case what you do is you you have the ability to design a graphql schema that is similar to
[1021.24 --> 1026.44]  your rest models but that also reflects the requirements of what the front-end developers want
[1026.44 --> 1031.40]  and so you can kind of design that graphql schema and then you can build that out and then you can map
[1031.40 --> 1035.26]  that now depending on the framework that you're using there are different approaches for doing
[1035.26 --> 1041.46]  this one of the common approaches today is to have a graphql schema and then build manually write a
[1041.46 --> 1046.46]  graphql schema which is a different language so it's a different language altogether uh you you have a
[1046.46 --> 1051.68]  file and inside that you write the graphql schema that kind of becomes a url or the routes file right
[1051.68 --> 1058.10]  uh that's one approach uh the other approach is if you are for example you have a java if you have
[1058.10 --> 1063.70]  some kind of typed language right let's say you have java or um i think now maybe type script these
[1063.70 --> 1069.40]  languages you are already modeling the resources right and in these cases very often like for
[1069.40 --> 1074.08]  example with spring boot you you might not even be explicitly creating rest api endpoints right you
[1074.08 --> 1080.16]  might just be creating models um and uh the rest api endpoints are almost auto-generated right um and in
[1080.16 --> 1084.50]  these cases actually what you can do is you can you know you can just build your models and these
[1084.50 --> 1089.70]  models will generate the graphql schema and the graphql api automatically for you in this case uh
[1089.70 --> 1094.28]  you know it basically your graphql schema reflects the kind of models that you have and that kind of
[1094.28 --> 1099.36]  ends up working as well so this is kind of like the different ways that you have um on the monolithic
[1099.36 --> 1107.76]  side um when you have microservices uh graphql becomes very painful uh to use um and uh this is this is
[1107.76 --> 1112.56]  actually a point of stress for the community at the moment which is you know how how do we deal with
[1112.56 --> 1117.44]  graphql and microservices i feel uh there are many there are many different approaches that have
[1117.44 --> 1123.64]  emerged a very common approach is the graphql gateway approach um and which is very very similar to the
[1123.64 --> 1129.52]  back-end for front-end approach so the bff approach right so what you do is you say um i'm going to
[1129.52 --> 1135.44]  build uh there's you take out a small team like a team of two or three people um or you you know maybe
[1135.44 --> 1141.38]  the front-end developers kind of decide to put together this team uh and this team now builds a
[1141.38 --> 1148.00]  graphql server uh and this graphql server uh provides the kind of graphql schema and graphql api
[1148.00 --> 1152.70]  for the front-end developers or for the different applications that are being used uh and on the
[1152.70 --> 1158.46]  back it queries these different microservices uh that you already have i think the best practice for
[1158.46 --> 1166.08]  using graphql is what would give you uh what really works for you uh and i think it's very similar
[1166.08 --> 1170.34]  again to the early days of rest where you know you have a lot of rest best practices and the way you
[1170.34 --> 1175.22]  should use rest verbs and the way you should do rest uh not model your resources but once rest
[1175.22 --> 1180.38]  became an api that was used everywhere you know people started crafting their rest api to be more
[1180.38 --> 1185.92]  suitable to what they wanted to do and you know what their application was doing um and it automatically
[1185.92 --> 1190.82]  kind of went through changes right so there's a lot a lot of convention that emerged around different
[1190.82 --> 1194.86]  kinds of domains and how to use the rest api properly and what to do with the rest api
[1194.86 --> 1199.22]  um and we are going to go through that journey with graphql as well um where we'll see many
[1199.22 --> 1205.24]  different kinds of use cases and best practices and patterns emerge around those use cases um for
[1205.24 --> 1212.92]  for how you can use graphql so you have built a company to have the team to use graphql for a cloud
[1212.92 --> 1218.64]  native application have you seen any interesting usage of graphql it's been a fascinating journey for us
[1218.64 --> 1225.80]  you know we're a we're an open source engine we launched just about a year ago um and you know
[1225.80 --> 1233.06]  kind of uh it's a graphql engine that you know works with the postgres database um and we've now added the
[1233.06 --> 1237.88]  capability of it to be able to talk to other microservices um so that you can kind of connect
[1237.88 --> 1243.80]  different microservices together and create a unified graphql endpoint um and uh and our graphql
[1243.80 --> 1249.60]  engine takes care of being able to kind of you know join across uh these services or join across
[1249.60 --> 1256.60]  what i call mid-tier services and databases um and provide um an authorization kind of system so that
[1256.60 --> 1262.42]  you can uh you can expose the right parts of the graphql schema to the right end users right sometimes
[1262.42 --> 1266.60]  you don't want to expose the whole graphql schema um and you're able to enforce certain authorization
[1266.60 --> 1272.14]  policies um there is another transformation that is happening in the world you know today which is
[1272.14 --> 1278.40]  the whole cloud native transformation uh you know movement from containers to uh making containers
[1278.40 --> 1283.84]  stateless right uh and to to even serverless functions which is kind of like you know the extreme
[1283.84 --> 1289.98]  uh of a microservice right that is an entire movement that is happening uh in one part of the
[1289.98 --> 1297.04]  industry so the backend developers are moving towards being event-driven uh of being decoupled having
[1297.04 --> 1302.12]  services having microservices having serverless functions right of using you know multiple
[1302.12 --> 1308.96]  sas apis they use vendor products uh they use uh they use an api created by another team so um so
[1308.96 --> 1314.60]  that is kind of that is kind of one entire uh industry movement that is happening powered by docker
[1314.60 --> 1318.84]  and kubernetes and all of the cloud native innovation that is happening and on the other end you know
[1318.84 --> 1323.40]  there's the front-end team uh and the front-end team wants graphql and graphql works really well with
[1323.40 --> 1329.18]  a monolith right uh but it does not work really well with microservices or serverless functions or whatever
[1329.18 --> 1335.20]  um and so there's been a tremendous amount of interest uh in trying to figure out how we can
[1335.20 --> 1341.88]  make both of those landscapes work well together right um in a naive way to connect a graphql api to
[1341.88 --> 1347.38]  various serverless functions and microservices is not hard but to actually make that work at scale to
[1347.38 --> 1353.42]  deal with performance to deal with caching to deal with security um it it's it requires a new form of
[1353.42 --> 1358.82]  thinking uh for the organization to actually make graphql work really well uh you know with a with a
[1358.82 --> 1364.02]  quote unquote cloud native back end by cloud native i mean you know things that are uh microservices and
[1364.02 --> 1369.20]  serverless functions and that are event driven so that are stateless um and and there's been a
[1369.20 --> 1375.40]  tremendous amount of interest in trying to make that work together uh so so the short answer is yes
[1375.40 --> 1380.38]  there's a huge amount of interest in trying to make sure that we can we can get the best out of
[1380.38 --> 1385.74]  graphql for the application development team and we can get the best out of our back end um and
[1385.74 --> 1390.62]  back end agility right um and back end is a loose word right it means everything may be on the
[1390.62 --> 1395.14]  infrastructure and get a tremendous amount of developer agility uh on on the back end as well
[1395.14 --> 1402.60]  excellent so you touch base a little bit of graphql and microservices and talk about how your company is
[1402.60 --> 1408.54]  trying to solve this issue i wonder though like what what are the pains and learning uh between
[1408.54 --> 1417.36]  you well using graphql for microservices you're right right um i think so um so sorry you know like
[1417.36 --> 1423.84]  like like i was i was mentioning a little bit before um a graphql api is uh powered by a graphql schema
[1423.84 --> 1430.44]  um and the graphql schema is essentially like a type system right um and so if you if you come from
[1430.44 --> 1434.80]  uh if you if you programmed in a you know type language kind of environment or statically typed
[1434.80 --> 1440.58]  environment you notice that you create types um you build types or you build classes uh right
[1440.58 --> 1444.00]  and functionally maybe you build types or maybe you're building classes and objects and things
[1444.00 --> 1449.28]  like that um and then as you're building things uh you know let's say you make an error uh in
[1449.28 --> 1453.86]  in the name of particular type right or the way you're referring to a particular type so maybe like
[1453.86 --> 1459.16]  the user type has an address uh field and the address field is pointing to an address type or a user
[1459.16 --> 1464.10]  class and an address class um and let's say you make a spelling error uh inside the way you refer
[1464.10 --> 1469.48]  to the address class from the user class um when you build it your compiler will tell you you know
[1469.48 --> 1477.60]  what here's a problem uh there is no such thing as uh adris right you spelled address like this this
[1477.60 --> 1481.98]  thing does not exist um and so what you do as a developer is you're like oh okay i need to go fix
[1481.98 --> 1487.74]  that and so you go fix it or maybe somebody else who's building a different module uh they named the
[1487.74 --> 1491.62]  they named their class user as well and so now when they try to build it they're like hey duplicate
[1491.62 --> 1497.14]  declaration right don't uh what's happening um and so then you as developers coordinate and you talk
[1497.14 --> 1503.62]  to each other uh and you fix this problem um but when you think about graphql with microservices
[1503.62 --> 1511.42]  each microservice defines their own set of apis right um and and when you try to bring them together
[1511.42 --> 1516.76]  with graphql what you're trying to say is hey these are the various types of microservice one these are
[1516.76 --> 1521.66]  the various resources by microservice two and these are maybe the relationships between microservice one
[1521.66 --> 1527.40]  and two between the types exposed by microservice one and two now the problem is that if you kind of
[1527.40 --> 1533.24]  think about the tooling of how these two microservices and types come together um this is very challenging
[1533.24 --> 1537.40]  right because the same problems that i talked about like maybe you are maybe you want to connect
[1537.40 --> 1543.34]  the user type to the address type uh how how do you keep track of the fact that the type names are
[1543.34 --> 1547.66]  evolving or changing or that there are errors in the references that you've created right so maybe
[1547.66 --> 1552.38]  when you dynamically build a graph how do you know that um it actually makes sense right there's
[1552.38 --> 1558.70]  actually there are actually services um that are handling this this it the problem moves out from the
[1558.70 --> 1563.98]  build time and moves into like the run time right and and that's just more challenging to deal with
[1563.98 --> 1569.98]  um and um and so that's kind of just maybe one example but you can have all kinds of problems with
[1569.98 --> 1574.30]  overlapping types so you can have like duplicate declarations and stuff like that yeah thank you
[1574.30 --> 1582.06]  for sharing your experience with uh graphql and microservices currently there's a working draft of uh
[1582.06 --> 1589.74]  the graphql spec what's new what's coming up next there are lots of discussions that are happening uh in
[1589.74 --> 1595.10]  the graphql spec in the graphql draft around how to be able to um you know namespace things or whether we
[1595.10 --> 1600.86]  should do it in graphql or not or when you think about graphql mutations and input types uh of
[1600.86 --> 1606.30]  whether we want interfaces for input types or not um and so there's a lot of active discussion there uh
[1606.30 --> 1614.14]  but but for the most part the bulk of the graphql spec has is uh is is very solid um a lot of a lot of
[1614.14 --> 1619.34]  the stuff that you need to do that you need to build is all pretty much done there are a few nuances that i
[1619.34 --> 1623.42]  think are being worked out um and i think there's a lot of pressure from the graphql and microservices side of
[1623.42 --> 1629.50]  things um to move the graphql spec in a particular direction but so far graphql is very solid and the
[1629.50 --> 1635.66]  and the spec is really solid is there any topic that you would like to cover that is not covered today
[1635.66 --> 1641.18]  i would urge folks to go try out graphql and learn graphql so and that's that's really easy to do
[1641.18 --> 1646.38]  uh at least to learn about graphql right whether you decide to use it or not uh tremendous amount
[1646.38 --> 1650.78]  lots of resources to be able to kind of quickly build an application of graphql on the front end or use
[1650.78 --> 1655.42]  a graphql api on the front end or uh you know build a small graphql server just to get a flavor of what
[1655.42 --> 1661.34]  it takes um and and i know i mentioned a lot of challenges with graphql uh but you know i i
[1661.34 --> 1666.30]  absolutely love graphql and i think it's uh it's going to be amazing so it's important for us as a
[1666.30 --> 1673.02]  community to you know get hands-on uh and and experience the benefits of graphql um use a graphql api
[1673.02 --> 1679.18]  integrate a graphql api understand the nuances of graphql uh uh and uh and then i think that'll help the
[1679.18 --> 1683.42]  community kind of evolve and figure out uh what the different kinds of things we can do with graphql
[1683.98 --> 1686.54]  what is the best way to learn about graphql
[1689.02 --> 1692.78]  there are there are many different resources depending on what you're trying to do um i think
[1692.78 --> 1696.62]  on the depending on the language of the framework that you're using if you're a back-end developer
[1697.02 --> 1704.22]  um you there are several nice tutorials uh you can just uh if you just search for uh like this
[1704.22 --> 1708.62]  there's something called awesome graphql which has a bunch of resources uh on the specific back-end
[1708.62 --> 1714.06]  framework and what kind of uh graphql library you can use and they usually have some nice tutorials
[1714.06 --> 1719.18]  um on the front-end side of things uh there are lots of there are lots of courses on egghead
[1719.90 --> 1727.10]  that have a nice introduction to graphql or udemy we maintain an open source uh set of tutorials on
[1727.10 --> 1733.74]  learn.hostler.io where you can uh kind of take two hours to learn how to integrate graphql into your react
[1733.74 --> 1741.18]  app as a react developer so we have tutorials for react angular flutter reason ml elm typescript uh
[1741.74 --> 1747.82]  and ios android and react native as well uh all maintained by the community uh and kind of helps you
[1747.82 --> 1754.62]  get started with graphql super fast the best way to to find resources for graphql is usually to scope
[1754.62 --> 1758.54]  it in by the specific technology stack that you want to be interested in
[1758.54 --> 1764.54]  um if you generally want to get a flavor for what the graphql api is um you can head to the
[1764.54 --> 1771.58]  graphql.org website um but from my personal experience um reading about graphql did not
[1771.58 --> 1776.06]  help me as much as when i used graphql to build a front-end application and that's when things
[1776.06 --> 1781.50]  started kicking for me um so i would encourage you to kind of build something with graphql especially on
[1781.50 --> 1787.58]  the front end to understand the power of graphql thank you for joining us today tamar it was has been a
[1787.58 --> 1794.62]  really useful conversation with you on graphql thank you for having me thanks for joining us
[1794.62 --> 1800.70]  for this episode of the codish podcast codish is produced by heroku the easiest way to deploy
[1800.70 --> 1806.14]  manage and scale your applications in the cloud if you'd like to learn more about codish or any of
[1806.14 --> 1815.18]  heroku's podcasts please visit heroku.com podcasts
[1817.58 --> 1824.62]  from here
[1824.62 --> 1828.06]  in
[1828.06 --> 1830.58]  here
[1830.58 --> 1832.62]  here
[1832.62 --> 1835.26]  here
