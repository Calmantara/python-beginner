from flask import Flask, jsonify, request, Response
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

# global variable
users_data = []
# https://pypi.org/project/flask-swagger/


# Swagger documentation route
@app.route("/swagger")
def get_swagger():
    swag = swagger(app)
    swag["info"]["version"] = "1.0"
    swag["info"]["title"] = "py-users"
    return jsonify(swag)


@app.route("/users", methods=["POST"])  # type: ignore
def post_users():
    """
    Create new User
    ---
    tags:
      - users
    definitions:
      - schema:
          id: Group
          properties:
            name:
             type: string
             description: the group's name
    parameters:
      - in: body
        name: body
        schema:
          id: User
          required:
            - email
            - name
          properties:
            email:
              type: string
              description: email for user
            name:
              type: string
              description: name for user
            address:
              description: address for user
              schema:
                id: Address
                properties:
                  street:
                    type: string
                  state:
                    type: string
                  country:
                    type: string
                  postalcode:
                    type: string
            groups:
              type: array
              description: list of groups
              items:
                $ref: "#/definitions/Group"
    responses:
      201:
        description: User created
        content:
          application/json
            schema:
              id: Success
              type: object
              properties:
                message:
                  type: string
                  example: ok
      400:
        description: Bad request
        content:
          application/json
            schema:
              id: BadRequest
              type: object
              properties:
                message:
                  type: string
                  example: invalid user body
    """
    body = request.get_json()
    users_data.append(body)
    return Response(
        {"status": "ok"}, status=201, headers=[("Content-Type", "application/json")]
    )


# @app.route("/users", methods=["GET"])  # type: ignore
# def get_users():
#     """
#     Get All Users
#     ---
#     tags:
#       - users
#     definitions:
#       - schema:
#           id: Group
#           properties:
#             name:
#              type: string
#              description: the group's name
#     responses:
#       200:
#         description: All Users
#         schema:
#     """
#     body = request.get_json()
#     users_data.append(body)
#     return Response(
#         users_data, status=200, headers=[("Content-Type", "application/json")]
#     )


# Swagger UI route
SWAGGER_URL = "/swagger-ui"
API_URL = "/swagger"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "py-users"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run("0.0.0.0", 3000)
