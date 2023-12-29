from flask import Blueprint, request
from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    result = search_users(request.args.to_dict())
    return result if result else [], 404
    #return {"result":result}, 200 if result else 404


def search_users(args):
    """Search users database
    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    matching_users = []
    
def search_users(args):
    matching_users = [
        user
        for user in USERS
        if (
            ("id" not in args or args["id"] == str(user["id"]))
            and ("name" not in args or args["name"].lower() in user["name"].lower())
            and (
                "age" not in args
                or (
                    int(user.get("age", 0)) >= int(args["age"]) - 1
                    and int(user.get("age", 0)) <= int(args["age"]) + 1
                )
            )
            and (
                "occupation" not in args
                or args["occupation"].lower() in user.get("occupation", "").lower()
            )
        )
    ]

    sorted_users = sort_search_results(matching_users, args)
    return sorted_users

#bonus challenge
def sort_search_results(users, args):
    priority_order = ["id", "name", "age", "occupation"]
    def sort_key(user):
        for field in priority_order:
            if field in args and user[field] == args[field]:
                return priority_order.index(field)
        return len(priority_order)
        
    sorted_users = sorted(users, key=sort_key)
    return sorted_users