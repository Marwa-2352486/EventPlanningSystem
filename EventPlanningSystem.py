"""The EventFactory class has methods to create events and guests."""
from abc import ABC, abstractmethod


class ICreateFactory(
    ABC
):  # An interface for Event Factory. two functions are passed down to the subclass.
    @abstractmethod
    def create_event(self, name, date, time, organizer, description):
        pass

    @abstractmethod
    def create_guest(self, name, rsvp=False, plus_one=False, dietary_req=None):
        pass


"""The Event class has a name, date, time, organizer, and description, and it also has a list of guests, venue and a menu.
The class has methods to add guests and view the list of guests."""


class Event:
    def __init__(self, name, date, time, organizer, description):
        self.name = name  # Assign the parameter "name" to the instance variable "name"
        self.date = date  # Assign the parameter "date" to the instance variable "date"
        self.time = time  # Assign the parameter "time" to the instance variable "time"
        self.organizer = organizer  # Assign the parameter "organizer" to the instance variable "organizer"
        self.description = description  # Assign the parameter "description" to the instance variable "description"
        self.venue = []  # New list to add venues
        self.guests = (
            []
        )  # Create an empty list and assign it to the instance variable "invitees"
        self.menu = Menu()  # Yus need to add comment
        self.track_guest_meals = {}  # Yus to add comment

    def add_guest(self, guest):
        self.guests.append(
            guest
        )  # Add the parameter "guest" to the list stored in the instance variable "guests"

    def view_guests(self):
        for (
            guest
        ) in (
            self.guests
        ):  # Iterate through the list stored in the instance variable "guests"
            print(guest)  # Print each guest

    def select_venue(self, venue):  # Add a method to set the venue for the event
        self.venue = venue


"""The Guest class has a name, RSVP status, whether or not they are bringing an additional guest, and any dietary requirements. 
The class has a __str__ method that formats the guest's information into a human-readable string."""


class guest:
    def __init__(self, name, rsvp=False, additional_guest=False, dietary_req=None):
        self.name = name  # Assign the parameter "name" to the instance variable "name"
        self.rsvp = rsvp  # Assign the parameter "rsvp" to the instance variable "rsvp" with a default value of False
        self.additional_guest = additional_guest  # Assign the parameter "additional_guest" to the instance variable "additional_guest" with a default value of False
        self.dietary_req = dietary_req  # Assign the parameter "dietary_req" to the instance variable "dietary_req" with a default value of None

    def __str__(self):
        return f"Name: {self.name}, RSVP: {'Yes' if self.rsvp else 'No'}, Plus One: {'Yes' if self.additional_guest else 'No'}, Dietary Requirements: {self.dietary_req}"


"""The Menu class has a dictionary of items, where each item is a meal and the value is a list of guests.
The class has methods to add items and view the menu."""


class Menu:
    def __init__(self):
        self.items = (
            []
        )  # Create an empty list and assign it to the instance variable "items"

    def add_item(self, meal):
        self.items.append(
            meal
        )  # Add the parameter "meal" to the list stored in the instance variable "items"

    def view_menu(self):
        for meal in self.items:
            print(meal)


class Venue:
    def __init__(self, name, rating=0):  # Add a rating attribute to the Venue class
        self.name = name
        self.rating = rating

    def __str__(self):
        return f"Venue: {self.name}, Rating: {self.rating}"


class EventFactory(ICreateFactory):
    def create_event(self, name, date, time, organizer, description):
        return Event(
            name, date, time, organizer, description
        )  # creates and returns an Event object with the given name, organizer, and description.

    def create_guest(self, name, rsvp=False, additional_guest=False, dietary_req=None):
        return guest(
            name, rsvp, additional_guest, dietary_req
        )  # creates and returns an Invitee object with the given name, rsvp, additional_guest, and dietary_req.


"""The EventView class has methods to create events, add guests, view the list of guests, add menu items,
and view the menu, add venue and rate the venue. The class uses an EventFactory object to create events and guests."""


class EventView:
    def __init__(self, event_factory):
        self.event_factory = event_factory  # Assign the parameter "event_factory" to the instance variable "event_factory"
        self.events = (
            []
        )  # Create an empty list and assign it to the instance variable "events"

    def create_event(self):
        name = input(
            "Enter event name: "
        )  # Prompt the user for input and assign it to the variable "name"
        date = input(
            "Enter event date: "
        )  # Prompt the user for input and assign it to the variable "date"
        time = input(
            "Enter event time: "
        )  # Prompt the user for input and assign it to the variable "time"
        organizer = input(
            "Enter organizer name: "
        )  # Prompt the user for input and assign it to the variable "organizer"
        description = input(
            "Enter event description: "
        )  # Prompt the user for input and assign it to the variable "description"

        if (
            name.strip() == ""
            or date.strip() == ""
            or time.strip() == ""
            or organizer.strip() == ""
            or description.strip() == ""
        ):
            print("Please provide all values. Try Again")
        else:
            event = self.event_factory.create_event(
                name, date, time, organizer, description
            )  # Create an Event object using the "event_factory" instance variable and the input from the user
            self.events.append(
                event
            )  # Add the newly created event object to the list stored in the "events" instance variable
            print(
                f"Event {name} created successfully!"
            )  # Print a message confirming the event has been created

    def additional_guest(self, event_name):
        event = next(
            (x for x in self.events if x.name == event_name), None
        )  # Iterate through the list stored in the instance variable "events" and return the first event object whose "name" attribute matches the parameter "event_name" or return None
        if event:
            name = input(
                "\nEnter additional guest name: "
            )  # Prompt the user for input and assign it to the variable "name"
            rsvp = (
                input(
                    "Has additional guest RSVPd? (y/n) *Pressing enter to skips will be considered <No>"
                ).lower()
                == "y"
            )  # Prompt the user for input, convert it to lowercase, and check if it is equal to "y" and assign the boolean value to "rsvp"
            dietary_req = input(
                "Enter guest dietary requirements: "
            )  # Prompt the user for input and assign it to the variable "dietary_req"

            if name.strip() == "" or dietary_req.strip() == "":
                print("Please provide all values. Try Again")
            else:
                guest = self.event_factory.create_guest(
                    name, rsvp, False, dietary_req
                )  # Create a guest object using the "event_factory" instance variable and the input from the user, with the additional_guest attribute set to true
                event.add_guest(
                    guest
                )  # Add the newly created guest object to the list of guests of the event
                print(
                    f"guest {name} added to event {event_name} as additional guest"
                )  # Print a message confirming the guest has been added as additional guest.
        else:
            print(
                f"Event {event_name} not found."
            )  # Print an error message if the event is not found

    def add_guest(self):
        event_name = input(
            "Enter event name: "
        )  # Prompt the user for input and assign it to the variable "event_name"
        if event_name.strip() == "":
            print("Please provide a proper event name")
        else:
            event = next(
                (x for x in self.events if x.name == event_name), None
            )  # Iterate through the list stored in the instance variable "events" and return the first event object whose "name" attribute matches the input event_name or return None
            if event:
                name = input(
                    "Enter guest name: "
                )  # Prompt the user for input and assign it to the variable "name"
                rsvp = (
                    input(
                        "Has guest RSVPd? (y/n) *Pressing enter to skip will be considered <No>"
                    ).lower()
                    == "y"
                )  # Prompt the user for input, convert it to lowercase, and check if it is equal to "y" and assign the boolean value to "rsvp"
                dietary_req = input(
                    "Enter guest dietary requirements: "
                )  # Prompt the user for input and assign it to the variable "dietary_req"
                additional_guest = (
                    input(
                        "Is guest bringing an additional guest? (y/n) *Pressing enter to skips will be considered <No> "
                    ).lower()
                    == "y"
                )  # Prompt the user for input, convert it to lowercase, and check if it is equal to "y" and assign the boolean value to "plus_one"
                if name.strip() == "" or dietary_req.strip() == "":
                    print("Please provide all values")
                else:
                    if additional_guest:
                        self.additional_guest(
                            event_name
                        )  # If the guest is bringing an additional guest, call the additional_guest method and pass the event_name
                    guest = self.event_factory.create_guest(
                        name, rsvp, additional_guest, dietary_req
                    )  # Create an guest object using the "event_factory" instance variable and the input from the user
                    event.add_guest(
                        guest
                    )  # Add the newly created guest object to the list of guests of the event
                    print(
                        f"guest {name} added to event {event_name}"
                    )  # Print a message confirming the guest has been added
            else:
                print(
                    f"Event {event_name} not found."
                )  # Print an error message if the event is not found

    def view_guests(self):
        event_name = input(
            "Enter event name: "
        )  # Prompt the user for input and assign it to the variable "event_name"
        if event_name.strip() == "":
            print("Please provide a proper event name")
        else:
            event = next(
                (x for x in self.events if x.name == event_name), None
            )  # Iterate through the list stored in the instance variable "events" and return the first event object whose "name" attribute matches the input event_name or return None
            if event:
                event.view_guests()  # call the view_guests method on the event object
            else:
                print(
                    f"Event {event_name} not found."
                )  # Print an error message if the event is not found

    def add_menu_item(self):
        event_name = input(
            "Enter event name: "
        )  # Prompt the user for input and assign it to the variable "event_name"
        if event_name.strip() == "":
            print("Please provide a proper event name")
        else:
            event = next((x for x in self.events if x.name == event_name), None)
            if event:
                meal = input(
                    "Enter meal name: "
                )  # Prompt the user for input and assign it to the variable "meal"
                if meal.strip() == "":
                    print("Please provide a proper meal name")
                else:
                    event.menu.add_item(meal)
                    print(
                        f"Meal {meal} added to event {event_name}"
                    )  # Print a message confirming the meal has been added
            else:
                print(
                    f"Event {event_name} not found."
                )  # Print an error message if the event is not found

    def view_menu(self):
        event_name = input(
            "Enter event name: "
        )  # Prompt the user for input and assign it to the variable "event_name"
        if event_name.strip() == "":
            print("Please provide a proper event name")
        else:
            event = next(
                (x for x in self.events if x.name == event_name), None
            )  # needs commenting
            if event:
                event.menu.view_menu()
            else:
                print(
                    f"Event {event_name} not found."
                )  # Print an error message if the event is not found

    def search_guest(self):
        guest_name = input(
            "Enter guest name: "
        )  # Prompt the user for input and assign it to the variable "guest_name"
        if guest_name.strip() == "":
            print("Please provide a proper name")
        else:
            for (
                event
            ) in (
                self.events
            ):  # Iterate through the list stored in the instance variable "events"
                guest = next(
                    (x for x in event.guests if x.name == guest_name), None
                )  # Iterate through the list of guests of the event and return the first guest object whose "name" attribute matches the input guest_name or return None
                if guest:
                    print(
                        f"guest {guest_name} found in event {event.name}"
                    )  # Print a message with the event name where the guest is found
                    print(f"RSVP: {guest.rsvp}")  # Print the guest RSVP status
                    print(
                        f"additional guest: {guest.additional_guest}"
                    )  # Print the guest and additional guest status
                    print(
                        f"Dietary Requirements: {guest.dietary_req}"
                    )  # Print the guest dietary requirements
                    return
            print(
                f"guest {guest_name} not found."
            )  # Print an error message if the guest is not found

    def view_events(self):
        for event in self.events:
            print(event.name)  # Print out all the events stored in self.events.

    def select_menu(self):
        event_name = input(
            "Enter event name: "
        )  # Prompt the user for input and assign it to the variable "event_name"
        if event_name.strip() == "":
            print("Please provide a event name")
        else:
            event = next((x for x in self.events if x.name == event_name), None)
            if event:
                guest_name = input(
                    "Enter your name : "
                )  # If the event exists, prompt the user for input and assign it to the variable "guest_name"
                if guest_name.strip() == "":
                    print("Provide a proper name")
                else:
                    for event in self.events:
                        guest = next(
                            (x for x in event.guests if x.name == guest_name), None
                        )
                        if (
                            guest
                        ):  # If the event exists in the list of events and if the list of guest contains the variable guest_name, start the while loop.
                            while (
                                True
                            ):  # The while loop will not end unless something returns False
                                if (
                                    len(event.menu.items) > 0
                                ):  # If the length of an item list is more than 0, continue.
                                    meal_name = input(
                                        "What are you having? : "
                                    )  # Prompt the user for input and assign it to the variable meal_name
                                    if (
                                        meal_name in event.menu.items
                                        and meal_name.strip() != ""
                                    ):  # If the given meal_name from the guest is in the menu, order is successful and the guest_name and the ordered meal get stored.
                                        event.track_guest_meals[guest_name] = meal_name
                                        print("Ordered Successfully")
                                        return False
                                    else:
                                        print(f"{meal_name} not found. try again.")
                                        return True
                                else:
                                    print("Add menu before selecting menu.")
                                    return False
                        else:
                            print(f"{guest_name} is not in the guest_list")
            else:
                print(f"Event {event_name} not found.")

    def track_meals(self):
        event_name = input(
            "Enter event name: "
        )  # Prompt the user for input and assign it to the variable event_name
        if event_name.strip() == "":
            print("Please provide a event name")
        else:
            event = next((x for x in self.events if x.name == event_name), None)
            if (
                event
            ):  # If the event exists, Go through the dictionary of track_guest_meals using for loop.
                for guest, meal in event.track_guest_meals.items():
                    print(
                        f"{guest}: {meal}"
                    )  # Print out the result of track_guest_meals
            else:
                print(f"Event {event_name} not found.")

    def select_event_venue(self):
        event_name = input("Enter event name: ")
        event = next((x for x in self.events if x.name == event_name), None)
        if event:
            venue_name = input("Enter venue name: ")
            event.select_venue(Venue(venue_name))
            print(f"Venue {venue_name} added successfully for event {event_name}")
        else:
            print(f"Event {event_name} not found.")

    def rate_venue(self):
        venue_name = input("Enter venue name: ")  # Add a method to rate a venue
        venue = next(
            (x for x in [event.venue for event in self.events] if x.name == venue_name),
            None,
        )
        if venue:
            rating = float(input("Enter rating for the venue (0-5): "))
            if 0 <= rating <= 5:
                venue.rating = rating
                print(f"Rating set successfully for venue {venue_name}")
            else:
                print("Invalid rating. Please enter a number between 0 and 5.")
        else:
            print(f"Venue {venue_name} not found.")


def main():
    # Create an instance of the EventFactory class
    event_factory = EventFactory()
    # Create an instance of the EventView class, passing in the event_factory object
    event_view = EventView(event_factory)
    # Run a loop to display menu options to the user
    while True:
        print("1. Create Event")
        print("2. Add Guest")
        print("3. View Guests")
        print("4. Search Guest")
        print("5. Add Menu Item")
        print("6. View Menu")
        print("7. Choose Meal")
        print("8. Track Meals")
        print("9. View Events")
        print("10. Add Venue")
        print("11. Rate Venue")
        print("12. Exit")
        # Get the user's choice of menu option
        choice = input("Enter your choice (1-12): ")
        # Check the user's choice and call the corresponding method from the event_view object
        if choice == "1":
            event_view.create_event()
        elif choice == "2":
            event_view.add_guest()
        elif choice == "3":
            event_view.view_guests()
        elif choice == "4":
            event_view.search_guest()
        elif choice == "5":
            event_view.add_menu_item()
        elif choice == "6":
            event_view.view_menu()
        elif choice == "7":
            event_view.select_menu()
        elif choice == "8":
            event_view.track_meals()
        elif choice == "9":
            event_view.view_events()
        elif choice == "10":
            event_view.select_event_venue()
        elif choice == "11":
            event_view.rate_venue()
        elif choice == "12":
            break
        else:
            print("Pick a number from above !!!!")


if __name__ == "__main__":
    # Check if the script is being run as the main program
    # If so, call the main() function
    main()
