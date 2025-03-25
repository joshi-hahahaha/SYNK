import React from "react";

const SettingsModal = () => {
  return (
    <dialog id="settings_modal" className="modal">
      <div className="modal-box">
        <h3 className="font-bold text-2xl">Settings</h3>
        <p className="py-4">This will have:</p>
        <ul>
          <li>light/dark</li>
          <li>profile</li>
          <li>login/register or sign out</li>
        </ul>
      </div>
      <form method="dialog" className="modal-backdrop">
        <button>close</button>
      </form>
    </dialog>
  );
};

export default SettingsModal;
