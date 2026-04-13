• Definition of Object Relational Mapping (ORM) and its purpose
• Discussion of the pros and cons of using ORMs, including custom SQL vs ORM queries
• Introduction to Joist ORM, a new ORM created by Stephen Haberman
• Background on why Joist was developed, including issues with existing ORMs such as TypeORM and MicroORM
• Explanation of how Joist addresses common problems with ORMs, including data loading and business logic encapsulation
• The speaker's frustration with ORMs (Object-Relational Mappers) and their lack of transparency about loaded collections
• Joist's goal to build a data loader from day one for every lazy-loaded call
• Representing the two states of a collection in the type system, including being unloaded until populated with a hint
• The novelty of Joist changing the types based on load hints, rather than defaulting to safe behavior
• Data loaders and their concept of automatic batching and promise-based loading
• The Facebook Data Loader library and its use of event loops to optimize wire calls
• Data loader pattern: accumulate and batch queries for efficient data loading
• Combining and uncombining data: combining queries into a single query and demultiplexing results
• Joist's global view vs per-table accumulation of queries
• Deriving properties and calculations in-memory vs strictly from the database
• Treating derived collections and fields as database literals in joins
• The benefits and drawbacks of using type hints to indicate if data is pre-loaded or not in an asynchronous model.
• A utility that could flatten out synchronous data into a format that can be worked with directly.
• Joist's ability to handle data loading and aggregation, potentially as a central pivot point for the data loader function.
• The potential complexity of implementing an async-agnostic system for joining multiple levels of data.
• Exploring possibilities for delaying or deferring loading of certain data until it is explicitly requested by the user.
• Relations in Joist are objects that can be either loaded immediately or lazily loaded
• Using preload hints can change the type of an object to include get methods for relations
• The difference between .get and .load is that .get will throw an error if the data is not already loaded, while .load will wait for the data to load
• Joist's design prevents N+1 queries by forcing developers to be explicit about when data is loaded
• Joist allows for different implementations of one-to-one relationships compared to one-to-many or many-to-many relationships
• Joist separates generated code from custom logic, with two classes: a visible, modifiable class for custom logic and an invisible, automatically generated class for boilerplate code.
• Relationships are defined by foreign keys and are mirrored in the generated code.
• The generated code is updated every time database migrations are run, ensuring it always matches the current schema.
• Joist does not generate code at runtime like Active Record; instead, it uses a codegen step to create the classes.
• The generated classes have lifecycle hooks (e.g., before update, before delete) and validation rules that can be used for business logic.
• The entity manager is a per-request cache of data, which helps with performance and simplifies caching.
• Joist's validation rules and how they can be used to ensure data consistency
• Managing cycles in hooks and the approach Joist takes to avoid infinite loops
• Batching and when the batch is sent to the database (explicit call via emflush)
• Per-request caching and how it works, particularly with GraphQL servers
• Visibility into requests and whether Joist can catch unflushed changes at the end of a request
• Middleware setup for entity managers and caches, and potential use for auto-flushing or auto-committing
• Legacy relational schemas and their impact on ORM usage
• The concept of treating tables as entities vs. joining entities with IDs
• Potential drawbacks of ORMs, including making SQL non-performant and allowing simplifying assumptions about database structure
• Joist's approach to solving the N+1 problem and its implications for ORM adoption
• The value of using ORMs for simple queries and the importance of knowing when to use low-level SQL or other tools for complex queries
• Standardization of lifecycles and validation
• Business invariance and data consistency
• Joist's concept of reactivity and reactive validation rules
• Reactive derived fields (e.g. author book count)
• Data loader baked into the system for easy data retrieval and caching
• Emflush autosaving derived entities and recalculating/revalidating as needed
• Joist's ability to string together reactive things using core database relations
• Limitations of bridging through entities in Joist
• Known issue with stacking non-core database relations
• Tagged IDs in Joist, including support for both strings and integers
• Joist's use of sequential integer primary keys in the database and tagged IDs at the application layer
• Support for UIDs as primary keys in Joist
• Comparison to Active Record and TypeORM