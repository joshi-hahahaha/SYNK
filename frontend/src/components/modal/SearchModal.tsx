import React from "react";

const SearchModal = () => {
  return (
    <dialog id="search_modal" className="modal">
      <div className="modal-box">
        <h3 className="font-bold text-lg">Search bar</h3>
        <p className="py-4">This will be a search bar with a drop down</p>
      </div>
      <form method="dialog" className="modal-backdrop">
        <button>close</button>
      </form>
    </dialog>
  );
};

export default SearchModal;
