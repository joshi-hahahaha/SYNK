import React from "react";

const EventsModal = () => {
  return (
    <dialog id="events_modal" className="modal">
      <div className="modal-box">
        <h3 className="font-bold text-2xl">Events</h3>
        <p className="py-4">
          This will have two tabs, one for the user events and the ones nearby
        </p>
      </div>
      <form method="dialog" className="modal-backdrop">
        <button>close</button>
      </form>
    </dialog>
  );
};

export default EventsModal;
