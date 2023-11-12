# Service_Oriented_Computing_Assignment_Application
Code Repository of Service Oriented Computing Assignment Application

1. The application comprises of multiple services, where each functional unit (user service, income service, and tax calculation service) is implemented as a separate service. Each service is responsible for specific functionality, and they communicate with each other as needed.
2. Each service exposes its own set of REST API endpoints, allowing seamless communication between services. This well-defined API structure enables clean and independent development, deployment, and scaling of each service.
3. To ensure data isolation and reduce inter-service dependencies, each service maintains its dedicated database. This approach enhances the autonomy of each service, minimizing the need for frequent cross-service calls and providing a more efficient and scalable solution.
4. To streamline user interaction with the various services, an API gateway is implemented. The API gateway serves as a unified entry point, allowing users to communicate with different services through a single interface. This abstraction simplifies the user experience and enables better control over service communication.
