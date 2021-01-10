import com.espertech.esper.common.client.EventBean;
import com.espertech.esper.runtime.client.EPRuntime;
import com.espertech.esper.runtime.client.EPStatement;
import com.espertech.esper.runtime.client.UpdateListener;

/** 实现UpdateListener接口，来定义事件的后置处理过程 **/
public class ListenerCoder implements UpdateListener {

    public void update(EventBean[] eventBeans, EventBean[] eventBeans1, EPStatement epStatement, EPRuntime epRuntime) {
        try {
            System.out.println("coder: name-"+eventBeans[0].get("name") + " age-"+eventBeans[0].get("age"));
        }catch(Exception e) {
            e.printStackTrace();
        }
    }
}


