import { EventObj } from "@/type";
import { FaCalendarAlt, FaClock, FaLock, FaGlobe } from "react-icons/fa";

export const EventPopup = (event: EventObj) => {
    const startDate = new Date(event.start);
    const endDate = new Date(event.end);

    // Calculate duration in hours
    const durationHours = Math.round((endDate.getTime() - startDate.getTime()) / (1000 * 60 * 60));

    return (
        <div className="relative p-1 transition-all duration-300">
            <div className="flex justify-between items-start">
                <h2 className="text-xl font-bold mb-2">{event.name}</h2>
            </div>

            <div className="mb-1">
                <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                    event.isPublic ? "bg-green-100 text-green-800" : "bg-red-100"
                }`}>
                    {event.isPublic ? (
                        <>
                            <FaGlobe className="mr-1" /> Open to Public
                        </>
                    ) : (
                        <>
                            <FaLock className="mr-1" /> Invite Only
                        </>
                    )}
                </span>
            </div>

            <p className="text-gray-600 mb-3 text-xs">
                {event.description}
            </p>

            <div className="space-y-3 mt-4 border-t pt-3">
                <div className="flex items-center">
                    <FaCalendarAlt className="text-gray-400 mr-2" />
                    <span className="text-gray-700">
                        {startDate.toLocaleDateString('en-AU', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })}
                    </span>
                </div>

                <div className="flex items-center">
                    <FaClock className="text-gray-400 mr-2" />
                    <span className="text-gray-700">
                        {startDate.toLocaleTimeString('en-AU', { hour: '2-digit', minute: '2-digit' })} - {endDate.toLocaleTimeString('en-AU', { hour: '2-digit', minute: '2-digit' })}
                        <span className="ml-2 text-gray-500">({durationHours} hour{durationHours !== 1 ? 's' : ''})</span>
                    </span>
                </div>
            </div>
        </div>
    );
};