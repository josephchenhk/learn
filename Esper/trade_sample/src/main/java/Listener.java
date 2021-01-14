import com.espertech.esper.common.client.EventBean;
import com.espertech.esper.runtime.client.EPRuntime;
import com.espertech.esper.runtime.client.EPStatement;
import com.espertech.esper.runtime.client.UpdateListener;

/** 实现UpdateListener接口，来定义事件的后置处理过程 **/
public class Listener implements UpdateListener {

    public void update(EventBean[] eventBeans, EventBean[] eventBeans1, EPStatement epStatement, EPRuntime epRuntime) {
        try {
            System.out.println("event: ts-"+eventBeans[0].get("ts") + " company-"+eventBeans[0].get("company") + " px-"+eventBeans[0].get("px"));
        }catch(Exception e) {
            e.printStackTrace();
        }
    }
}
