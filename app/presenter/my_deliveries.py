from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Clock

from model.delivery_request import DeliveryRequest, Status
from model.user_me_getter import UserMeGetter
from presenter.delivery_request_detail import DeliveryRequestDetail
from model.firebase.firestore import Firestore
from presenter.delivery_list import ListItem

from kivymd.label import MDLabel

Builder.load_file("view/my_deliveries.kv")


class MyDeliveries(BoxLayout):
    """
    Widget that lists all delivery requests accepted by the user.

    Each request is represented with a ListItem.
    """

    def __init__(self, **kwargs):
        """Initializes the delivery list"""
        super(MyDeliveries, self).__init__(**kwargs)
        Firestore.subscribe(
            u'users/{}/deliveries'.format(UserMeGetter._user_id),
            self._pre_update_content)

    def _pre_update_content(self, collection_snapshot, _, __):
        Clock.schedule_once(lambda x: self._update_content(collection_snapshot)
                            )

    def _update_content(self, collection_snapshot):
        """Fetch all deliveries the current owner has accepted"""
        delivery_requests = []
        for doc in collection_snapshot:
            data = doc.to_dict()
            data['uid'] = doc.id
            data['status'] = Status(data['status'])
            delivery_requests.append(DeliveryRequest(**data))

        # Fill delivery list
        self.ids.my_deliveries.clear_widgets()
        no_content = True
        for req in delivery_requests:
            if req.status == Status.DELIVERED:
                continue

            no_content = False
            self.ids.my_deliveries.add_widget(
                ListItem(req, self._transition_to_detail_view))

        # Add no content label if no content is shown
        if no_content:
            no_content_label = MDLabel(
                text="""You currently do not have any packages to deliver.\n
                Accept deliveries by searching for them.                  """,
                size_hint_y=9,
                halign="center",
                font_style='Subtitle1')
            self.ids.content.add_widget(no_content_label)

        self.content = self.ids.content

    def _transition_to_detail_view(self, request: DeliveryRequest):
        """Show detail view for selected delivery request."""
        self.clear_widgets()
        self.add_widget(
            DeliveryRequestDetail(
                back_button_handler=self._transition_to_my_deliveries,
                request=request))

    def _transition_to_my_deliveries(self):
        """Show list of all available deliveries."""
        self.clear_widgets()
        self.add_widget(self.content)
