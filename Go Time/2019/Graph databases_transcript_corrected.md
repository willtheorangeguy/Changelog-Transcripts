**Mat Ryder:** Hello, and welcome to Go Time. I'm Mat Ryder, and today we're talking about Graph databases. Joining me is Johnny Tourniquet. Hello, Johnny!

**Johnny Tourniquet:** Hello, Mat.

**Mat Ryder:** We're also joined by Jana B. Logan. Hello, Jana.

**Jana Logan:** Hello!

**Mat Ryder:** How are you?

**Jana Logan:** Good!

**Mat Ryder:** Welcome back, it's been a while.

**Jana Logan:** It's been quite a while...

**Mat Ryder:** Yes. Well, it's good to have you back. We're also joined by a special guest, it's only Francesc Cambó. Hello, Frances!

**Francesc Cambó:** Hey, how's it going?

**Mat Ryder:** How are you?

**Francesc Cambó:** Pretty good. That was a decent pronunciation of my name. \[laughs\]

**Mat Ryder:** Well, thank you. That means a lot. Well, I'd like to start with one of the first questions that gets asked every time I mention you - it's from Pontus on Slack. He asks "When is JustForFunc coming back?"

**Francesc Cambó:** Um, eventually...? \[laughter\]

**Mat Ryder:** Great. Cool.

**Francesc Cambó:** Yeah, eventually coming back. Maybe next year. Maybe.

**Jana Logan:** Do you need help?

**Francesc Cambó:** Yeah, I need extra time. That's the only thing I need. \[laughs\] No, but now I finally moved to a new house and everything, and settling down, and I will have a little studio, so I will be able to start again. Now I just need the energy. So you know, a couple of months of relaxing, and then back.

**Mat Ryder:** Great. For everyone who doesn't know, which is probably nobody, there's a great video series that Frances does called JustForFunc. I'm fine that you picked that name. I suggested "Go Fun Yourself." \[laughter\] But that was rejected. You didn't like that one.

**Francesc Cambó:** Yeah... You know, back then I used to work at Google; not sure how that would have been accepted.

**Johnny Tourniquet:** Oh, Fun that... \[laughter\]

**Mat Ryder:** There's another one that got rejected... So today we're gonna talk about Graph databases, and this is a fascinating area, and it feels very new. We're going to dig into that a little bit more. But maybe we could start off with a simple overview, Frances, of what you're doing. Then we can go into what actually is a Graph database.

**Francesc Cambó:** \[04:04\] Yeah, so I can talk a little bit about how I got involved with Graph databases. After I left Google, I joined this company source{d}, where I started doing code analysis... And when you think about it, if you think about how you parse code, you end up with a tree, a syntactic tree... And the idea is once you start adding annotations on top, like "This function is calling the code in there" or "This variable was declared there" or "This is a type" or whatever, you start having a graph. And then you think about how are you going to store this, and you look up relational databases, and it's a bad match. It doesn't really work, it's super-hard to do, and as soon as you start adding more things, it just breaks; the schema needs to be very -- it's too strict.

So then you go into NoSQL databases, and then you have the issue of "How much do you replicate? Do you want to replicate the same information over a bunch of time for performance, but then you need to take into account the consistency, or do you want to put everything into little pieces, but then it's going to be super-slow? And that's when I started looking into Graph databases. And you're right, it sounds like it's somehow new. That said, how old do you think Neo4j is?

**Mat Ryder:** Oh, that's a good one. Johnny, what do you think?

**Johnny Tourniquet:** I'd say at least ten years...

**Francesc Cambó:** It is, if I'm not mistaken, 19 years old.

**Mat Ryder:** Wow!

**Francesc Cambó:** Yeah. So they've been going at it for a while.

**Mat Ryder:** It can nearly drink. \[laughter\]

**Francesc Cambó:** Yeah, I mean, in Spain it can definitely drink. \[laughter\] Yup. So it's not a completely new technology, but it's something that has been evolving over time, little by little, and I started looking around and there's not that many Graph databases, actually. Like, pure Graph databases. Databases that have a Graph layer - there's a bunch of them, there's a bunch of different competitors etc. But the problem is that storing things as a graph is actually something not that easy to do, and it's something that brings a lot of flexibility. Because the idea is that instead of having to -- you know if you think about a graph; let's say Twitter, the people that you follow, and the tweets, and the tags, and hashtags, and all that stuff - if you store that in a Graph database the same way you would draw it in a whiteboard, that's what you store. You store nodes, and you store relationships, and that's pretty much it.

As soon as you need to start thinking about "Oh, how do I model this so it fits my database?", you are adding complexity from the point of view of the developer. You need to think about these things, which is an important cost. People do not take that into account, but the complexity that you add to your system means that once you're going to start debugging, it's going to be harder to debug, because there's extra layers of abstraction.

And then on the other side it's also performance-wise. The way you're going to be able to retrieve things if you need to do transformations... If you think about a relational database - and we have people that follow people - if I tell you "Oh, find all the people that I follow, and then their followers, and then their followers", or something like that, you're going to go quite deep. It's going to be a bunch of different requests, and this is what people call the N+1 problem; the idea of "If I fetch something and then I want to fetch something related to those things that I've just fetched", you're going to have to do a query, start with that dataset, and then for every single item in the dataset do one more query. And it keeps multiplying. So it doesn't really scale. The idea of Graph databases is solving that problem specifically.

\[07:57\] So I started looking around, and I decided to join Graph partly because they're writing it in Go which is kind of cool. I think that people might like to Go in this podcast... And also it's completely open source, it's distributed, and it's also in San Francisco, which is nice, because I didn't want to travel that much.

**Mat Ryder:** That's interesting then. I want to talk more about this later, but you said it's distributed. As I understood it, one of the things that makes Graph databases quick is that it's kind of all stored in the format that -- it doesn't get transformed very much, does it? It's kind of stored in the format that you then use it with. Does that make sense?

**Francesc Cambó:** Yeah. So the whole idea - there's this term that people like to throw around, even though most people do not really understand what it means... It's called index-free adjacency. Index-free adjacency just means that when you're -- actually, there's a very good metaphor that I like to use... So in index-free adjacency, imagine that I'm Frances, and I'm trying to go to someone's house; I just know their address and I go there. That is index-free adjacency. You just have all the information from the beginning.

Well, in normal databases the way it's gonna work is I have a key that allows me to go check it out, where this information is, and then you go find it. So it's more like I go to someplace, like a phone book or something, I find the name of the person, I can find the address and then go get it. So that extra step - that is the main difference of how things are stored. But at the end of the day, the way we store data is key-value. It's just key-value store, that is extra-fancy, with a bunch of things on top, and raft consensus protocols, and things like that... But the way we store things at the end of the day is just key values, and the distributed part of things is the fact that many databases - Neo4j is one example - in order to be efficient, they need to store everything in the same machine.

At Graph what we do is instead we partition a dataset by the predicate. Say there are many predicates, like name, or age, or friends - that information is separate, so we're going to store it on potentially different machines. Not necessarily... You can have everything just on one machine, but it could be potentially on multiple machines. And the idea is that by separating the data like that, no matter how much data you're fetching, the number of fun-- fun calls, I was going to say... The number of network requests that you're sending is proportional to the number of predicates that you're fetching, not the amount of data, so it scales really well.

Otherwise, if you end up partitioning in any other way - at least the ones that we have tried - as you go with more data, you end up having to send queries to all the computers that are involved, and then that kills performance again.

**Jana Logan:** Can I ask a more fundamental question? Because I think I'm super unqualified to be on this podcast... \[laughter\] So compared to, for example, to column-based DBs, what is the overall underlying storage structure for a graph DB? ...in the same node, like let's say everything is just on one machine.

**Francesc Cambó:** Yeah, so it's kind of cool, because we use an open source project that was also created by Graph, which is called Badger... It's the project that gives name to our mascot, which is Iggy the badger. This is just a key-value store, so you could think about like SSTs, and things like that, like sorted string tables and all that stuff that we use at Google... But the idea is that from a high-level point of view you just have keys and values. The way these are actually implemented internally - it's an LSTM, which is a log-structured tree... What was it...? Log-structured tree...

**Mat Ryder:** Merge. Merge-tree.

**Francesc Cambó:** \[12:06\] Yes, merge-tree. I always mix it with long short-term memory, which is an AI thing, so... I mix everything. But yeah, what this structure allows you to do is to have a very good answer time, and also a very good retrieval time. So it's just a different kind of tree that we use. And if you've ever heard about Rocks DB, it's somehow similar to Rocks DB. The two biggest differences are 1) the values are not stored inside the tree, which means that it's more efficient from the point of view of storage, and also when you're iterating over queues it's much faster, because you don't need to fetch the values. And then the second one, which is more important - it's actually written in Go. And that for us was very important, because otherwise we had to use CGO. And CGO is great, but not really necessarily performant. So it was actually important to be able to have something that was working natively in Go. But yeah, it's just a fancy key-value store, at the end.

**Johnny Tourniquet:** One of the examples we've already touched on is the social graph, because that's an easy thing to wrap your head around. I'm interested to hear what are some of the uncommon examples that you've come across or Graph has come across in its customer base, for using this type of technology. What is it perfect at, beyond just social graph?

**Francesc Cambó:** Yeah, a social graph is the traditional example, because as soon as you talk graphs, people are like "Oh, Facebook, and Twitter", and all that stuff... Which is great. It actually works pretty well for those use cases. But in general, that is again a class of knowledge graphs; graphs where you're storing information. For instance, Graph actually comes from technology developed at Google. I think that internally the project was also called Graph... Which is weird, but it's okay, because Google never uses the internal name externally, or something like that, so it was cool...

But yeah, it is the same technology, and the idea is when you're storing information for movies, and actors, and all that stuff, if you think about the -- I think it's called One Box, which is when you search something, and you have on the right side of the search this extra information telling you the actor, and the movies they've been in, and stuff like that... That actually is served by a graph.

So the idea is in order to store that information and being able to retrieve things easily, graphs are the best way to do it. But then on top of that, that knowledge graph could be something that changes really fast. We have seen people doing knowledge graphs on -- it's like a visibility layer more than anything, on top of Kubernetes.

So if you think about Kubernetes, you have services, and pods, and all of these things. They're all related in many different ways. There are tags, there's traffic, there are services sending things around... You can't visualize that inside of Kubernetes and inside a graph database, and then query things like "Hey, what are the things that could impact this service if this service goes down or the other way around if this service goes down what pieces of my system would be impacted?" And that is a graph problem.

There's actually an open source project created by VMware. It's called Purser. And there are many others. There are things like actually geographic graphs... We have geolocation, so you can do things like "Find all the hotels that are at less than 50 miles from downtown of San Francisco", and then from there do more graph stuff. So you can go quite deep into finding things about your dataset that otherwise is just very hard... Because if you think about all of these queries, you could definitely do them anywhere. You could do them on a normal database, on a relational database. The problem is that it's going to be way, way slower.

\[16:08\] I don't know if you've ever used BigQuery. With BigQuery, you end up writing queries that run across terabytes of data... And it's not about the fact that it's easier to write, it's just that short developer loop... It's just much better. You get the feedback, and you keep on playing, while if you need to wait for five minutes it's going to be way, way slower and more painful.

One other use case that we see very often is since there's no need for a schema, you can actually integrate a bunch of different datasets together very easily. Dataset integration or dataset identification happens pretty often. Imagine you have a really large telecom company that has been acquiring different companies, and for every single one of those companies acquired probably there's a user base. There's an account database with a bunch of different things. And what you want to do is being able to integrate all of those systems together into one... Graph databases are great for that.

If you think about how you would do it with a relational database, the number of foreign keys that are going to be flying around is going to be a pain. So that kind of thing is also very useful. It's very simple, and it works really well.

**Mat Ryder:** We talked earlier about indexes, and this doesn't have that same kind of pattern... I was playing around recently with Firestone, which is the Firebase schema-less data store, and if you do query that you haven't done before, you actually get an error, and it says "I can't serve this because there's no index that matches the order of those fields", or whatever the filter is you're doing... So you kind of have to know in advance what you're going to be asking of this database. Is that different in graph databases because of its nature?

**Francesc Cambó:** Not necessarily. The whole idea is indexes are not necessary to traverse relationships. If I start from a given node, going around that node will not require an index. The place where you might need an index is to find that first node. The whole idea is that while you will not need indexes to traverse relationships, you might still need indexes to find those first initial nodes that you're gonna use to start your traversal. And there are a bunch of different things...

For instance, if you want to find all the orders, all the products that have been ordered by a given user, all of that does not require an index, but actually finding the user from their username - that will require one. So you do have indexes, and those indexes need to be built. They will not be built until you ask for them, but the idea if you're using Graph - I'm actually not that sure about other graph databases, but for Graph at least the way it works is that you start inserting data; you don't care about the schema... But there's a schema that is being created as you go. And then if you try to do a query that requires an index, and it's not there, it will indeed fail and tell you "Hey, you need to build this." You click a button, now you have an index... And then the idea is that while you're developing, that scheme is going to evolve over time.

And then at the end, that schema is something that you're actually going to put in your source code, and say "Okay, this is the schema that I'm going to be using." Then, once you send it into production, normally what I recommend is there's a strict mode for mutations; so when you're putting your data, you can actually say "Hey, if that data does not follow the schema that I already have, reject it." It's a much safer way to do it. For development, I think that schema-less databases are great. But then as soon as you get in production, I'd be a little bit more careful with that.

**Mat Ryder:** \[19:55\] I had the same thing -- I used to do MongoDB stuff, and it was the same... I couldn't believe that I didn't need to think about schemas; I can just do anything, and actually documents don't even have to look the same or even similar... And that freedom just felt so powerful then. Once I'd built a few things, I realized "I could really use some errors about now."

**Francesc Cambó:** Yeah. So the idea for us is that you can start with no schema at all, but we also have a type system on top... So the idea is you start adding things, and then you're going to say "Oh, this node has this type, and this type is supposed to have these fields..." It doesn't mean they have the fields, it just means that they should. So if you have a person, you could say "It's supposed to have a name, and then age." So then when you're fetching things, you're going to say "Fetch all the fields of type 'person'", or things like that.

So you can actually have a type system on top, and that is something completely optional. You can start from paying zero attention to the data you're storing in your database, see how it goes, end up with a schema, and then from that schema that contains all the predicates or all the kind of information that you stored - name, age, friends, all of those things - then you're going to go and say "Okay, is this actually the type that I want? Do I need indexes on this, or like a username? I'm going to find exact, or I'm going to use hash to find these things...", and then group those into types, and then you can start doing more advanced things.

The cool thing is that once you get there, then you can present that -- we have a GraphQL layer, so then you can actually start sending queries in GraphQL to your graph database, which makes is so... You know, front-end engineers are much, much happier when you tell them that they can use GraphQL instead of having to learn a new language.

**Break:** \[21:41\]

**Jana Logan:** Is there any additional calls of going completely schema-less? Because the indexes are going to be affected... How rebuilding the index works if you change the schema... Is this one of the reasons that on production you wanna actually lock the schema?

**Francesc Cambó:** \[23:57\] Not necessarily. The idea is that you can change your schema as you go. It's totally fine. If you want an index to something that didn't have an index, it will be computed on the fly... And it's fine; it's really fast also. But if you have terabytes of data, it might take a couple of minutes. During those minutes you will not be able to change your data; you will be able to only retrieve data, but not do mutations... Which is fine, but the idea is while you're doing the development, you're actually working normally with a smaller dataset, and at that point it's great, because then you can click and it's basically instantaneous.

So while you're developing that developer experience of schema-less, I really like it. It's somehow like when you're writing code, and you're writing in Python, the fact that you can just put things together, and it just works - that is great. But at the same time, when I'm going to production I want to have a little bit more rigidity, and make sure that the schema is working for me... So I'm gonna start adding things that will make it so if I do something wrong, which is totally possible, I will be notified. Some error, even if it's just a log, or a warning, or something like that, is much better than silently failing.

**Jana Logan:** Yeah, completely.

**Francesc Cambó:** So that's the idea of why I want -- I like the schema-less, and it's super-useful, but once I'm in production, I'd rather be writing Go with a decent type system than be writing C and end up having weird things happening if I'm doing something wrong. I have zero trust in me.

**Jana Logan:** It really happened to me when I was working with document DBs... Since there's no schema, I would just end up having all these embedded types, embedded objects. You can end up just really doing a lot of things wrong, especially if the references are referring large objects, or whatever. Everything just gets into the database, so it's kind of nice to have that option to restrict it to a schema.

**Francesc Cambó:** Yeah, I've had issues where after debugging for ten minutes I realized that the data I was storing had a typo in the name of the field, and that took me forever... So I was like "That is the kind of thing I just don't want to happen." If I can avoid that, much better for me. That's why having a schema that is optionally enforced makes a lot of sense.

**Jana Logan:** Yes.

**Johnny Tourniquet:** I'm to wrap my relational modelling head around not having to have a schema, and that's proving quite hard for me... How do you model relationships that are not just like "Oh, this piece is connected to this other piece by some sort of loose relationship between them"? How do I model things like actual relationships? Maybe I have an invoice with line items on it. This is kind of like a parent-child relationship, you can't have the line item just floating out and about; it belongs to something. It doesn't have meaning without the parent relationship... So how do you model these kinds of things? Or rather, do you have to throw that approach out the door, or leave it at the door before you entered a world of schemaless and a world of graph databases?

**Francesc Cambó:** I mean, you don't really need to get rid of all the concepts that you had before, especially if you're coming from a document database... If you come from a document database, imagine instead of having a document that is just a big JSON, you basically explode that into -- instead of having an object that has name and age, and then friends that point to an array of people that have name and age, you're going to explode that into little facts. So you're going to say "This ID has the name Frances, and then Age whatever, and then Friends is a list of different IDs, and then those IDs also have their name and age...", so you're going to break that into triplets. A triplet is subject, verb and object. So you're saying things about things, and that's what you store at the end. You literally store just that.

\[28:03\] Once you take that into account, you realize that all the ordering that you had is gone. So then if you have something like an order with items, and you want those items to be stored in some way, in a specific order, then you actually need to store that there. And you have different ways of doing this... You can create something like the way you would do it in a traditional relational database, where you're going to have this item-blind table that points to both the order and the product that they have, and then also has the item number in there, or something. That is a way to do it. But for us, you could do it just as a node; itself is a node, which is something similar to what you would think about the relational database, or you can also attach things, you can attach data to the relationships themselves. So you could say "This item belongs to this order", and that relationship - you're tagging it saying "It's item order number one."

So there are multiple places where you can store that kind of information, and the whole idea is very flexible, so you can do whatever you want, which means that you need to be a little bit more strict. You need to really think about how do you store this... And that's why having a schema is going to help you with those things. But at the end of the day, what we see is people mulling in the most straightforward way possible, like simplifying as much as possible. Then they start sending queries, and they start to see "Okay, these are the performance issues I'm hitting..." Because depending on the way you're storing data, you're going to get more or less performance. So that's when you start tuning your database.

But in general, I'd say that just storing the data the most natural way possible is the best way to go. Because it's like when you write in Go - you're not supposed to be thinking about cache locality right away. If you're doing that, your code is going to be hideous. Write code that makes sense to you, and that makes sense to everyone, that is easy to maintain, and then if we need to find a hack somewhere to fix it and make it much faster, then let's do that then... But not from the beginning.

And for data modelling I would say it's the same. Find something that is obvious and very clear, and if that doesn't work, first file an issue and let us know... Because maybe there's an issue, or something like that... But also, at that point we're going to start looking into performance turning and doing actual debugging and figuring out how much data are we fetching... Because sometimes it might be something as silly as "Oh, you're actually not using this index, and instead of loading one item, you're actually loading all of your database." That's not good. So that is the kind of thing that you need to look into as you're writing your thing... But data modelling should be as straightforward and as natural as possible... Because at the end of the day you're going to have to maintain that over time. So if you start getting smart, you're going to need to be at least as smart as you are now in a month, which I'm not convinced I can, so... \[laughter\]

**Jana Logan:** Good point.

**Johnny Tourniquet:** Along those lines... In my experience, you can go pretty far with a relational database before you start noticing that "Oh, I didn't have the proper index, and the right column..." You can go far before you realize "Okay, I have to do something about this. I have a problem with my actual data and how it's being stored." It sounds like with key-value stores, with graph databases you kind of have to put a bit more forethought into how we structure your data, like where it goes, how you're gonna shard, and things like that.

**Francesc Cambó:** \[31:48\] Actually, it's the other way around. I would say that graph databases (and document databases, too) the fact that the schema is so flexible makes it so eventually -- like, you go for the simplest way, and if you then need to migrate to something else because you find something that was not taken into account from the beginning, you can. It is actually doing transformations in the data and everything is pretty straightforward. While if you think about a relational database...

I have this example of you have movie and director, and what you're saying is "A movie has a director, so what I'm going to do is in the movie I'm going to put a foreign key pointing to the director that directed that movie." And you're like "Great!" You start working on that, and then you figure out that "Guess what - there are movies that have multiple directors." Now you need to refactor that database, and that is hard... Because the way you're storing the whole thing, it's going to be much harder to move out into different pieces.

You're going to need to come up with a new concept, "movie director", or something like that, that's somehow in between... Because now you go from one-to-many, to many-to-many." So all of those things are way harder to do, while for us if you say "Oh, these are one-to-many relationship", and then you're like "Oh, never mind, it was many-to-many", it's literally just changing the type of the predicate in one place. That's it.

Migration-wise, I think it's much easier. The whole idea is that you get to make those decisions once you have the information that you need to make those decisions, rather than from the beginning and trying to get it right.

**Mat Ryder:** So that has a massive development advantage, because actually I think we fool ourselves into thinking we can design these things perfectly in the beginning, and then there's an implementation phase, or whatever... And it's never like that. You learn so much by doing it, that actually being able to be adaptive and to migrate the data becomes very valuable. Andy Walker in the Slack channel -- Andy Walker is my new Twitter enemy... He was asking about what that switch between dev mode and prod mode looks like. He asks "Do I need a corpus of seed data that represents everything I care about, and then clear that out in some way and snapshot it, or something?" What's the actual process there?

**Francesc Cambó:** The way I normally do this - and there are different options, but the idea is that while you're inserting data in the database, by default you can insert any data and everything will be accepted. So you start putting things in there, and it's going to be creating a schema as you go. Say I store something saying my name is Frances - it's gonna store something saying "Oh, there's a thing called Name, and it points to a type..." It maybe guesses it's a string if you send it as JSON, or if you send it as a RTF, it's going to say "It's default. We don't know what it is, but you can store things in there."

As you go, you're going to start tuning that up, and saying "Actually, naming needs to be a string. And not only that, but we're also going to need an index." Or then you get age, and you keep on adding more and more data as you go. The whole idea is that eventually you have all the data that you need, that is ready in that schema... And then on top of that you also have your database with all the indexes that you need to do the queries that you're going to need to do. At that point, that schema that has been created automatically - you can literally copy-paste it into your code and call it Graph. Schema, and now what you're going to do is when you start your program if the database didn't exist - it's a completely blank database - you're going to send that schema and then lock it... And say "Okay, from now on this schema is not allowed to change." So if I want to send data that matches that, that's totally fine. But if you try to send data that instead of Name it uses First Name, which is not something I've said that you could use, it would just reject it.

So when you start the database, you have this switch that says -- it's the serving mode, and in serving mode there's standard, or strict. The other one is completely nothing - you cannot mutate anything, you cannot change the data. You get a read-only database. So it's somewhere in between. You can write things, but you cannot modify your schema.

**Jana Logan:** \[36:11\] Just because you mentioned read-only databases, is there any sort of replication of data? Can I have multiple read nodes, for example, and have one-write nodes, or...?

**Francesc Cambó:** Yes, that's actually a very good point. Graph - the D stands for Distributed. So the idea is that you are supposed to be running multiple servers for every single function; it is designed so it doesn't have any single point of failure. If you think about how Kubernetes works - you have multiple replicas, and those replicas in a group host the same information, they do the same thing, and we use the graph to decide which one is the leader. If one of them dies, we don't care. If you have three of them and one of them dies, you still have a quorum, you have two of them, so the database is going to continue working. And then once it comes back, it's going to be notified "Hey, you're part of this group. This is the data that you should be serving. So it catches up." So the data will be replicated.

But on top of that, if the amount of data that you have doesn't fit in a single machine, then you can start adding more groups, and then the data will be sharded across all of those groups. But again, they will have their own replicas and everything, so you're going to have what we call alphas, which are the servers that hold the data... You can have as many groups as you want, and in every group you normally have 3 or 5 replicas, depending on the availability expectations that you have. And then the same for the zeroes. And the zero is actually basically -- I think it's called Kubernetes Master, or something like that... The controller that manages the whole cluster - that one also you can replicate and have three, so if one goes down, the cluster is still working.

**Mat Ryder:** You mentioned earlier GraphQL, and I've seen GraphQL implementations that I was surprised to learn it was just backed by Postgres.

**Francesc Cambó:** Yeah.

**Mat Ryder:** But the interface is GraphQL. And like you said, JavaScript developers love that, because -- I mean, I think there's something nice about being able to specify exactly the kind of data that you want back, and nothing more... And also in quite a natural way, because the GraphQL is kind of a JSON format, Longish...

**Francesc Cambó:** Yeah.

**Mat Ryder:** So what do you think about that, having the graph interface into traditional databases?

**Francesc Cambó:** I think that GraphQL is a great alternative to REST. I really sincerely like it. It makes it, so there's a schema, so when you're requesting things, you know what you're allowed to be requesting... But at the same time, you also have not only the data, but also operations. So you have mutations, and queries, and things like that. So it's kind of like a nice, modern way of doing gRPC. If you've ever used gRPC where you have the data, which is represented as protocol buffers, but then you also have all the different -- I think they're called...

**Mat Ryder:** Services.

**Francesc Cambó:** Services, yeah... All the different services, right? So it's kind of a similar idea for GraphQL. So I like that a lot. That said, the problem is that it's a beautiful abstraction that is super-hard not to make it leak. If you have a very beautiful abstraction of "Oh, it's all one graph. Everything is a graph, you're just going to use everything as graphs" - okay, first problem is authentication. Huh. Fun. \[laughter\] If you start considering these things, there are actually many issues of implementing that in a very natural way.

\[39:51\] There are a lot of adaptors, like Prima, Apollo and Hasura are examples of different companies that provide adaptors on top of existing databases. That is great, because it means that you can create a GraphQL layer on top of your old system, and then eventually, little by little, start replacing things and say "Oh, these I'm going to move into this more GraphQL-native environment", or "I'm going to break this monolith into microservices, and just federation on top..." All of these things work and they're very useful.

That said, every single time I go to a GraphQL summit, people talk about the same issues of caching, the N+1 problem... Like, if you're fetching a lot of information, and you're based on top of a relational database, you're fetching all the data in the table basically no matter what. So you're going to be fetching that information, and then from there you're going to get a lot of data, and then before you send it, "Oh, guess what - on top of customers, now I want to get all the orders." So you're going to need to get those IDs and go down and get the information for the orders, and then go down again. So it's like that N+1 problem. And then in order to fix it, there are things like pre-fetching some things, and basically playing with caches, and things like that, and it becomes really rough. I mean, it works, which is great, but it is hard to understand and even harder to debug.

So that's why for us, for Graph, the GraphQL - it was super-easy to adapt, because our previous language that we support, and we will support for a long time, it's GraphQL+-, because it's more or less GraphQL. It's basically GraphQL, but adding some extra things to make it a better query language for a database, and then removing something that didn't make much sense.

So adapting GraphQL was super-easy - "it's basically the same language - and now what we're doing is figuring out "How can we bring the things that we added that make the language incompatible with GraphQL, how can we add them back to GraphQL in a compatible way?" And there are ways... It's super-interesting, actually. A lot of language design, and APIs, but inside GraphQL. Super-cool.

**Jana Logan:** Just because you mentioned debugging, in relational databases for example there's a huge culture around analysis tools... They can analyze your query, and so on. Do you have anything for Graph?

**Francesc Cambó:** Not right now. We're actually working on having a query planner. Right now the only places -- the thing is that the way the data is structured, query planners do not make that much sense, except on how you use indexes. So that is where we're starting working... Because sometimes using the index is not necessarily the best way to do it. Basically, if you have joins of two tables in relational databases, if one of them is much smaller than the other, there are better operations that you can do than just doing the full joint. So it's kind of the same idea, of like depending on the size of the datasets, sometimes using an index is better, sometimes just going and iterating over all the items might be faster... So that's the kind of things that we are looking into.

That said, in the latest version that we published we have a new thing that allows you to have an idea of how many nodes have been fetched, how much data from the disk you had to get, how many network calls you had to go through... And then on top of that - I'm sure you'll love it, Jana - we have Open Census absolutely everywhere.

**Jana Logan:** \[laughs\] Congratulations.

**Francesc Cambó:** Yeah, thank you. It works surprisingly well. When you go into like "Okay, so this is slow. What is going on?" and you just open Open Census and you can see all the traces hitting the different machines, hitting the disk and saying "This and this was really slow. What is going on in here?" That makes it so the tooling that we're developing on top will be useful for the end user, but for any knowledgeable person that already knows Open Census there's a lot already in there, thanks to open source.

**Jana Logan:** \[44:02\] It's also a knowledge tool. I really like distributed traces as a knowledge tool. It's probably so hard for everyone on the team to understand everything end-to-end, so they can just basically use distributed traces to learn more about their project, right...?

**Francesc Cambó:** Yeah. And that's also something that -- that is where I enjoy having control from... You know, let's say you're surveying a GraphQL layer. You have a GraphQL that is transforming into things that are sent to the alphas, and then talk to the zeroes, and then go to Badger and get something from an SSD... We own all of that code, so we're able to put Open Census across the whole thing and have a very clear view of what's going on.

**Jana Logan:** That's great.

**Francesc Cambó:** If you try to do something like that within an adaptor, and you have an adaptor over some other database, actually that integration is going to be super-hard.

**Jana Logan:** Yeah.

**Francesc Cambó:** So the fact that we simplify everything and everything is built by us, everything is in Go, everything Open Census, everything -- I'm going to go with the word "cloud-native"; the idea of everything is supposed to be running continuously, and if something crashes, whatever - just restart it and keep going. All of those things make it so at the end of the day it is much easier to use, because there's fewer moving pieces.

**Mat Ryder:** Somebody on Twitter the other day said Kubernetes was basically turning things off and on again at scale.

**Francesc Cambó:** Yeah, and it works.

**Break:** \[45:33\]

**Mat Ryder:** We should talk a bit about what you wouldn't use a graph database for as well...

**Francesc Cambó:** Yeah.

**Mat Ryder:** I think a lot of our listeners - and I for certainly will be doing this; I'm gonna go and play with this now, because I wanna really see... Because I still don't have a full understanding, from what we've talked about, of what this actually can do and what it feels like when you use it. But are there problems where you just wouldn't even think of using a graph database?

**Francesc Cambó:** I mean, the way we've built Graph was with general use cases in mind. You're storing data... Like, the same way you're using a document database -- you can use document databases for basically everything. It's a very general field. We're trying to make it so you can have graph algorithms and fancy things, but at the same time the normal use case of just storing data and then getting it back and making sure that everything is stable and performant - that's what we're going for.

That said, there are things like if you're doing time series data - there are much more efficient solutions for this, because it's a very specific field that has amazing solutions. So a time series is one of those... I would say analytics is something that we're able to do, depending on how much data you're throwing at it.

\[48:06\] If you're doing analytics in real time, I think that Graph is actually perfect for that. If you're doing analytics on larger data that you're basically batching and just going over all the data at the same time, BigQuery is great. Reimplementing that is going to be really hard. So some tools are going to be better at some specific use cases. I do think that people still have a very clear tendency to use relational databases for everything, and relational databases are really great for when you need to fetch a lot of information, that it's always the same schema, and things like that. Unfortunately, that's not the case that often. Relational databases are somehow quite bad at storing relations, even though it's in their name... They're not perfect at that.

**Mat Ryder:** North Korea is called The Democratic People's Republic of North Korea... \[laughter\]

**Francesc Cambó:** I mean, yeah... \[laughter\]

**Jana Logan:** We are cancelled in North Korea. Whoops... \[laughter\]

**Johnny Tourniquet:** Thanks, Mat... \[laughter\]

**Francesc Cambó:** At least someone in North Korea had a sense of humour... \[laughter\] Not, but it is hard to manage relations in a relational database sometimes, and that's why people enjoy document databases. It just makes it easier; you just store your data, and that's it. And I think that graph databases could be somehow like a substitute for document databases, that it's going to scale much better. So that's where I think it could go, yeah.

**Mat Ryder:** Do you think that people are going to end up with running different types of database in some cases, still having -- I mean, probably if people are transitioning, or if a team thinks "This is a perfect use case for this, but we still have this existing system that we have to live with..." Because you're not allowed to just delete everything and start again sometimes. So do you imagine that, that there's going to be situations where you would actually have your relational database (or whatever your existing data store already is) still running, but you also maintain the graph for those extra special specific cases?

**Francesc Cambó:** Yeah, that's actually something that we see pretty often, where you already have a very large dataset, and what you want to do is now get a read of that, because you already have so many programs, so many systems already using that database... So replacing that database means that you have to replace all the software on top of that, and that's a lot of work, something impossible to do. But what we try to do in those cases is to get a graph database next to your traditional database, and sync them together. Many databases are able to send a Kafka stream of mutations, so that "Hey, this has changed. This has changed..." So you can keep the graph database up to date completely with a relational database, and then use the graph database for the things that graph databases are good at.

A traditional example, if you have a blog system and you want to fetch all the comments for a given blog, and that was big data - that is actually really hard if you store it as comments on something, and that could be either a comment or a post. Having to do that - you're going to have to have an extra index for sure, but you're basically going backwards into how relational databases work. So it's going to be really hard, and not very performant. You could use that to just keep the metadata of all the indexes inside the graph database, and then fetch all the nodes or fetch all the IDs of the things that you want, keep that structure, and then the metadata of the tags, and images, and whatever is still in your relational database.

So using it as an index database that is going to enhance what you can build, rather than having to replace the whole thing. That's totally a normal thing, because you know if you go to a CTO, and you're like "Hey, I have this brand-new database. Replace yours with this one", they're going to be like "Yeah, no... We're not going to do that."

**Mat Ryder:** "Yeah, we're just gonna Ctrl+A and then Delete on everything we've got, if that's alright..." \[laughter\]

**Francesc Cambó:** \[52:11\] "Just store your data on this floppy disk, and then we'll go from there." \[laughter\]

**Mat Ryder:** So if we poked around in the files that are stored by Graph then, what does it actually look like? What is it literally when it's on disk, what does it look like?

**Francesc Cambó:** So, you're going to see that there are three directories - P, W and AW. So the P is where all the data is going to be stored. You're actually going to have LSTM files, so basically what Badger stores. A bunch of different key-value stores represent an LSTM in disk so you have a bunch of those... And then you have W, which is a write-ahead log. So every single demo operation is sent to the database, we're going to store it there, just in case it crashes. So if it crashes, then we can tell "Oh, this is where we were, these are the operations that we need to keep on applying."

And then there's one more folder, which is the AW. AW is the zero write-ahead log for the cluster itself. Zeroes are the ones that manage the cluster themselves. So you're going to have those three folders, and everything in there is just binary files. You could technically copy those and send them around and start a new database, but the problem is that these files are actually -- the way they work, they contain things like how many machines you have in your database cluster, and things like that... So over time, if you change that, probably you're going to end up having crashes, and that's not the way to go. But we also have things that you can export all of your data to JSON, or RTF, or you even have binary backups which store in protocol buffers.

**Jana Logan:** Is a file system the only way to store data, or can I just write an adaptor to send it to some blob store somewhere?

**Francesc Cambó:** So the idea is that Badger, the key-value store, is designed to work on SSDs. If you're not running on an SSD, it will still work, but it will be way slower. So the idea is that SSDs need to be there. When you're doing a backup, you can totally store that in a cloud storage, or whatever; that's totally fine.

The interesting thing is there was actually someone that was asking about how could they do it to store all the data in memory, and there's something that we're doing for Badger, for the key-value store, where we're going to have a diskless mode, where everything is stored in memory, and then you would be able to run everything on RAM... Which is not a great idea for a graph database that is supposed to store a lot of data, but if you have something tiny that you want a really high performance on, it's definitely something that you could try.

**Jana Logan:** Is it possible to use in FS, or do you have to write a new adapter?

**Francesc Cambó:** Oh, it's already built... What we're doing is not adding a lot of things, we're basically removing some checks that we had. There were some blocks that were storing on disk and some small things that we had to remove. By default - yeah, we already have adapters to write everything directly in memory. You don't need to do anything.

**Jana Logan:** That's cool.

**Mat Ryder:** If the data-- sorry, Johnny. If the dataset -- I don't know why I apologize to you, because the listeners didn't know you had the hand up, did they...

**Johnny Tourniquet:** I don't think... Nope, they didn't.

**Mat Ryder:** It's hard. This job is hard. \[laughter\] And to top it off, I forgot what I was going to say, so... Over to you, Johnny. \[laughter\]

**Francesc Cambó:** What a great host. \[laughs\]

**Johnny Tourniquet:** I'm telling you... \[laughs\]

**Mat Ryder:** London calling... It's like there's a big delay as well, although there isn't. This is amazing, sorry. We'll cut this bit out; sometimes I just get amazed that technology works, so... This is one of those times. Johnny...

**Johnny Tourniquet:** \[56:05\] Not, this bit will be left in, I promise you... \[laughter\]

**Mat Ryder:** Anything where I look stupid stays in. That seems to be the policy.

**Johnny Tourniquet:** \[laughs\] So on episode \#103 actually we had some folks from Graph on the show; we had Manish Jain and Karl McGuire... And we talked about a lot of things, including ristretto. I'm sure I'm butchering that... You can correct me when you answer this, but... I believe the idea was to introduce a perfect cache that could serve the needs of Graph under the hood. I'm interested in hearing the state of that transition, and whether it's been done already, or how things are going, how things are performing... Furthermore, I'm interested in hearing about that.

**Francesc Cambó:** Yeah, technically if you want to go Italian, you're going "Ristretto", but otherwise we would say ristretto... It's much easier. \[laughter\] So ristretto is this caching mechanism that we're integrating at different levels. One of the levels is actually in the key-value store. We're going to have an integration with Badger directly... And the idea here is that we've added encryption and compression to the key-value store, which makes it harder on the CPU. So when you need to decrypt things before you can read them, that's the CPU taking extra cycles... So the idea is that by having a cache, we will make it be as fast as before by using a little bit more memory.

Then on top of that we're also adding it at Graph level, and we're even thinking about using it at GraphQL level... So then we could have caching on many different levels, and trying to see what is the most performant option. The interesting thing about ristretto is that writing a cache in Go is actually really hard. It is surprisingly hard. Questions like -- you know if I give you a pointer to a struct that has a bunch of things, how much space does it take in memory? That is super-hard to answer.

**Mat Ryder:** The pointer?

**Francesc Cambó:** No, what is behind the pointer. You have a struct, but then of course, it's the sum of the fields, sure. Plus aligning, and things like that... And then what is the size of a map? Well, it's the size of all the keys, plus some extra stuff... What is the size of a slice? Well, it's the array, plus some extra stuff... So you get "plus some extra stuff" in so many places that actually figuring out -- given, for instance, if you have a JSON file, and you want to parse it, and say with certain accuracy "How big is this going to be once I pass it in memory?", that is surprisingly hard.

So when you're doing this for a cache, if you don't get that right, the problem is that you cannot really tell whether these new objects fit in memory or not. So should you drop something before you log this one or not? It is hard. Even gRPC -- gRPC works really well, but gRPC doesn't really do this either in Go. For C++ there's this concept of arenas, where you can code objects directly into a memory space... But in Go it doesn't do this, it doesn't support it. So all of these things, like memory and management in Go, are surprisingly complicated... Which is fun, but also it's like -- I've seen some issues where I was like "I literally have no idea. I don't know how to help you with this, so... Good luck."

**Mat Ryder:** And of course, none of your old Google friends will talk to you anymore, so you can't even ask them then...

**Jana Logan:** \[01:00:00.08\] Why am I here on this show? \[laughter\]

**Francesc Cambó:** That's a good question... \[laughter\] My god. But yeah, with ristretto the whole idea is to make Badger better and Graph better, and being able to use memory in a way that compensates for the extra cost in CPU... But also at the same time we wanted to make it open source, so anyone can use it for whatever they feel like it. And it's pretty successful. A lot of people have been adopting it, filing issues and feature requests and things like that, which is really nice to see.

**Mat Ryder:** Yeah, I'm actually using it now in a project.

**Francesc Cambó:** Oh, nice.

**Mat Ryder:** Yeah. It is great. And it's such a simple kind of API as well. It's really easy to just plug in. And it's so satisfying when suddenly your application is just extremely fast. It's very satisfying. I don't look at the RAM; I'll just get more RAM if I need some more RAM, that's my approach... But others like to be a little bit more scientific... \[laughter\]

So I'll just spell that out if anyone is interested... And we will post these links in the show notes, but it's "Ristrrrrreto", isn't it? Ristretto...

**Francesc Cambó:** Do you know what a ristretto is at least?

**Mat Ryder:** Is it a type of pasta? And I'm not being rude... \[laughter\] I genuinely-- it's making me hungry.

**Francesc Cambó:** Because it sounds Italian, it's pasta? \[laughter\]

**Mat Ryder:** Well, I thought it was...

**Jana Logan:** Is it like a coffee?

**Francesc Cambó:** No, a ristretto is a very, very short espresso. It's like a tiny coffee.

**Jana Logan:** Oh, yeah.

**Mat Ryder:** Oh. Espressos are really tiny though, aren't they?

**Francesc Cambó:** Yeah, so a ristretto is even smaller. It's a couple drops of coffee.

**Mat Ryder:** It is like an espresso for kids.

**Francesc Cambó:** I think if you feed your kids' ristretto, you end up with someone like you at the end. Like, I would not feed ristretto to my kids... \[laughter\] It seems like a bad idea.

**Jana Logan:** Yeah, it's like the same amount of coffee, but it's shorter, so it's really dense, right?

**Francesc Cambó:** Yeah.

**Jana Logan:** Something like that...

**Francesc Cambó:** It's compressed coffee, yeah.

**Mat Ryder:** Sorry, I got told off for suggesting it was pasta, but it turns out it was coffee... Come on! \[laughter\]

**Francesc Cambó:** But yeah, the whole idea is to make something very small that works well, so ristretto is a good name.

**Mat Ryder:** Yeah. It is great. I recommend people try it. It's so easy to plug into existing Go projects as well, indeed. Thank you so much for educating us, Frances. What's the domain name for people that want to find out more about what you're doing?

**Francesc Cambó:** Dgraph.io. Also, before we finish, I wanted to mention something... There's FOSDEM coming up, you may have heard about it - this open conference in Belgium, that happens in February 1st and 2nd, if I'm not mistaken... And this year again I'm co-managing it with Marthe Eskers from Women Who Go. The CFPs are open, so please apply. We want to have as many proposals as possible, so at the end we'll get perfect, high-quality talks. They end up being given at a very small venue, because the conference is always super-crowded, and it's fun, but then also we end up with very nice videos... So even if it's your first time speaking, it's a great place to try it out. Also, you will have people helping you, mentoring you, previewing your slides and helping you rehearse, whatever it needs. So first-time speakers are totally welcome, and are actually encouraged to apply.

**Mat Ryder:** Brilliant, thank you very much. We will post all of these links in the show notes, so don't worry... And all that leaves is for me to say goodbye. Thank you, everybody. Thanks for listening. We'll see you next time!
