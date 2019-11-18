using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Growl.Connector;
using PrettyGood.Util;

namespace Seymour
{
    internal class Message
    {
        GrowlConnector growl = new GrowlConnector();
        Application application;

        bool useGrowl;

        readonly string appname;

        public Message(bool useGrowl)
        {
            appname = App.ReadableAppName;
            this.useGrowl = useGrowl;

            if (useGrowl)
            {
                application = new Application(appname);

                growl.ErrorResponse += new GrowlConnector.ResponseEventHandler(growl_ErrorResponse);

                var v = new List<NotificationType>(Reflect.MembersOf<NotificationType, Message>(this));
                growl.Register(application, v.ToArray());
            }
        }

        void growl_ErrorResponse(Response response)
        {
            Gui.message(String.Format("Growl: {0} - {1}", response.ErrorCode, response.ErrorDescription), System.Windows.Forms.MessageBoxIcon.Error);
        }

        private void notify(NotificationType type, string id, string title, string text)
        {
            if (false == useGrowl) return;

            Notification n = new Notification(appname, type.Name, id, title, text);
            growl.Notify(n);
        }

        public void notifyNewMessage(string id, string title, string text)
        {
            notify(newMessage, id, title, text);
        }

        public NotificationType newMessage = new NotificationType("NEW_MESSAGES", "New messages");
    }
}
